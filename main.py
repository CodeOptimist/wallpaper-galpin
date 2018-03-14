import requests, json, os, re, math, glob, tempfile, pytz, tzlocal, time
import PIL.ImageOps
from PIL import Image
from collections import OrderedDict
from datetime import datetime, timedelta
from autohotkey import AutoHotkey
from gen.ShObjIdl_core import IDesktopWallpaper, DWPOS_SPAN
from comtypes.client import CreateObject


sub = 'earthporn'
url = "http://www.reddit.com/r/{}/top.json?t=week&limit=100".format(sub)
after = ""
required_fit_percent = 0.00
app_dir = os.path.join(os.getenv('APPDATA'), 'wallpaper-galpin', sub)
tmp_dir = os.path.join(tempfile.gettempdir(), 'wallpaper-galpin', sub)
sub_json_path = os.path.join(app_dir, sub + '.json')
sub_json = None
app_json_path = os.path.join(app_dir, sub + '-local.json')
app_json = None
last_updated_at = datetime.min


def init():
    global app_json, sub_json, last_updated_at
    try:
        os.makedirs(app_dir)
        os.makedirs(tmp_dir)
    except FileExistsError:
        pass

    app_json_defaults = {'last_updated': 0, 'accepted': [], 'rejected': []}
    try:
        with open(app_json_path, 'r') as f:
            app_json = json.load(f)
    except FileNotFoundError:
        app_json = app_json_defaults
    for k, v in app_json_defaults.items():
        if k not in app_json:
            app_json[k] = v

    try:
        with open(sub_json_path, 'r') as f:
            sub_json = json.load(f)
    except FileNotFoundError:
        pass

    PROCESS_PER_MONITOR_DPI_AWARE = 0x2
    ahk.execute('DllCall("Shcore.dll\SetProcessDpiAwareness", Int, {})'.format(PROCESS_PER_MONITOR_DPI_AWARE))


def main():
    global app_json, after

    just_ran = True
    while True:
        monitors, screen = get_monitor_info()
        update_every_m = 60 * len(monitors)
        print("Monitors: '{}' Update frequency: '{}'".format(len(monitors), str(timedelta(minutes=update_every_m))[:-3].zfill(5)), end='\r', flush=True)

        clock_interval_m = math.gcd(update_every_m, 60)
        update_due_at = get_last_updated_at(clock_interval_m) + timedelta(minutes=update_every_m)
        is_update_due = datetime.now(pytz.utc) > update_due_at
        on_the_mark = datetime.now(pytz.utc).time().minute % clock_interval_m == 0
        is_machine_idle = ahk.f('A_TimeIdlePhysical') / 1000 / 60 >= update_every_m
        if is_update_due and (just_ran or on_the_mark and not is_machine_idle):
            just_ran = False
            print()
            fetch_json()
            old_tmp = list(glob.glob(os.path.join(tmp_dir, '*.*'), recursive=False))
            if load_wallpaper(monitors, screen):
                after = ""
                app_json['last_updated'] = datetime.now(pytz.utc).timestamp()
            with open(app_json_path, 'w') as f:
                json.dump(app_json, f, indent=4)
            for entry in old_tmp:
                if os.path.isfile(entry):
                    os.remove(entry)
        else:
            # noinspection PyTypeChecker
            update_in = update_due_at - datetime.now(pytz.utc) + timedelta(minutes=1)
            update_in -= timedelta(microseconds=update_in.microseconds)
            print("Monitors: '{}' Update frequency: '{}' Next update in: '{}' at: '{}'".format(
                len(monitors),
                str(timedelta(minutes=update_every_m))[:-3].zfill(5),
                str(update_in)[:-3].zfill(5),
                update_due_at.astimezone(tzlocal.get_localzone()),
            ), end='\r', flush=True)
        time.sleep(30)


def get_last_updated_at(clock_interval_m):
    dt = datetime.utcfromtimestamp(app_json['last_updated']).replace(tzinfo=pytz.utc)
    dt_rounded = round_time(dt, timedelta(minutes=clock_interval_m))
    return dt_rounded


def round_time(dt, round_to, func=math.floor):
    dt = dt.replace(microsecond=0)
    s = (dt - dt.replace(hour=0, minute=0, second=0)).total_seconds()
    round_s = round_to.total_seconds()
    rounded_s = func((s + round_s / 2) / round_s) * round_s
    diff = timedelta(seconds=rounded_s - s)
    result = dt + diff
    return result


def fetch_json():
    global sub_json
    json_url = "{}&after={}".format(url, after)
    print(datetime.now(), "fetching", json_url)
    try:
        response = requests.get(json_url, headers={'User-Agent': 'Python 3.6.1 (Windows NT 10.0):wallpaper-galpin:v2.0 (by /u/CodeOptimist)'}, timeout=5)
        sub_json = response.json()
    except Exception:
        time.sleep(60 * 3)
        return False
    with open(sub_json_path, 'w') as f:
        json.dump(sub_json, f)
    return True


def load_wallpaper(monitors, screen):
    global after
    wallpaper = Image.new("RGB", (screen['w'], screen['h']))
    for idx, monitor in monitors.items():
        mon_rejected = 'rejected_{}_{}'.format(monitor['w'], monitor['h'])
        if mon_rejected not in app_json:
            app_json[mon_rejected] = []

        try:
            for _json_attempt_idx in range(2):
                for img_json in sub_json['data']['children']:
                    img_name = os.path.basename(img_json['data']['url'])
                    already_seen = any(img_name in app_json[k] for k in ('accepted', 'rejected', mon_rejected))
                    if already_seen:
                        continue

                    try:
                        img, img_path = get_img(img_json, monitor)
                        fit_img = PIL.ImageOps.fit(img, (monitor['w'], monitor['h']), PIL.Image.LANCZOS)
                        name, ext = os.path.splitext(os.path.basename(img_path))
                        fit_img.save(os.path.join(tmp_dir, name + '_fit' + '.png'))
                        print(datetime.now(), "found", idx, os.path.basename(img_path), img_json['data']['title'])
                        wallpaper.paste(fit_img, (monitor['x'] - screen['x'], monitor['y'] - screen['y']))
                        app_json['accepted'].append(img_name)
                        raise ImageSuccess
                    except MonitorImageRejectedError:
                        app_json[mon_rejected].append(img_name)
                    except ImageRejectedError:
                        app_json['rejected'].append(img_name)
                after = sub_json['data']['after']
                fetch_json()
        except ImageSuccess:
            continue
        return False

    wallpaper_path = os.path.join(app_dir, 'wallpaper.png')
    wallpaper.save(wallpaper_path)

    set_wallpaper(wallpaper_path)
    return True


def set_wallpaper(wallpaper_path):
    # # doesn't work due to limitation of calling AutoHotkey.dll from Python (uses SendMessage/PostMessage):
    # # "An outgoing call cannot be made since the application is dispatching an input-synchronous call."
    # ahk.execute("""
    #     ptr := ComObjCreate("{C2CF3110-460E-4fc1-B9D0-8A1C0C9CC4BD}", "{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}")
    #     vTbl := NumGet(ptr + 0, 0, "Ptr")
    #     setWallpaper := NumGet(vTbl + 0, 3 * A_PtrSize, "Ptr")
    #     setPosition := NumGet(vTbl + 0, 10 * A_PtrSize, "Ptr")
    # """)
    # ahk.execute('DllCall(setWallpaper, "Ptr", ptr, "Str", "", "Str", "{}")'.format(wallpaper_path))
    # ahk.execute("""
    #     DWPOS_SPAN := 5
    #     DllCall(setPosition, "Ptr", ptr, "Int", DWPOS_SPAN)
    #     ObjRelease(ptr)
    # """)

    com_obj = CreateObject('{C2CF3110-460E-4fc1-B9D0-8A1C0C9CC4BD}', interface=IDesktopWallpaper)
    com_obj.SetWallpaper(None, wallpaper_path)
    com_obj.SetPosition(DWPOS_SPAN)
    com_obj.Release()


def get_monitor_info():
    screen = get_screen_info()
    monitors = OrderedDict()
    for idx in range(1, screen['num'] + 1):
        monitors[idx] = {}
        ahk.execute(r'SysGet, mon{0}, Monitor, {0}'.format(idx))
        l, t, r, b = [int(ahk.get('mon{}{}'.format(idx, side))) for side in ("Left", "Top", "Right", "Bottom")]

        monitors[idx]['x'] = l
        monitors[idx]['y'] = t
        monitors[idx]['w'] = r - l
        monitors[idx]['h'] = b - t
    return monitors, screen


def get_screen_info():
    result = {}
    SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN, SM_CMONITORS = (76, 77, 78, 79, 80)
    for c, n in zip(('x', 'y', 'w', 'h', 'num'), (SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN, SM_CMONITORS)):
        ahk.execute(r'SysGet, result, {}'.format(n))
        result[c] = int(ahk.get('result'))
    return result


class ImageSuccess(Exception):
    pass


class ImageRejectedError(Exception):
    pass


class MonitorImageRejectedError(Exception):
    pass


def get_img(img_json, monitor):
    img_url = img_json['data']['url']
    if '//imgur.com/' in img_url:
        img_url = img_url.replace('//imgur.com/', '//i.imgur.com/') + '.jpg'
    if not img_url.endswith(r'.jpg') and not img_url.endswith(r'.jpeg'):
        raise ImageRejectedError

    title = img_json['data']['title']
    link_flair_text = img_json['data']['link_flair_text'] or ''
    dimension_re = r'[\[(]\s*(?P<w>\d+)\s*\D\s*(?P<h>\d+)[)\]]'
    m = re.search(dimension_re, link_flair_text)
    if m is None:
        m = re.search(dimension_re, title)

    if m:
        # can't tell for certain before downloading whether dimensions are given as WxH or HxW
        w = int(m.group('w'))
        h = int(m.group('h'))
        if min(w, h) < min(monitor['w'], monitor['h']):
            raise MonitorImageRejectedError
        if max(w, h) < max(monitor['w'], monitor['h']):
            raise MonitorImageRejectedError

    img_path = fetch_img(img_url)
    img = Image.open(img_path)
    img.load()  # immediately closes file

    w, h = img.size
    if w < monitor['w'] or h < monitor['h']:
        raise MonitorImageRejectedError

    is_oriented_same = (monitor['w'] / monitor['h'] >= 1) == (w / h >= 1)

    img_ar = w / h
    mon_ar = monitor['w'] / monitor['h']
    fit_percent = (mon_ar * h) / w if img_ar >= mon_ar else (w / mon_ar) / h
    is_fit = fit_percent >= required_fit_percent

    if not is_oriented_same or not is_fit:
        raise MonitorImageRejectedError
    return img, img_path


def fetch_img(img_url):
    img_name = os.path.basename(img_url)
    img_path = os.path.join(tmp_dir, img_name)
    if not os.path.isfile(img_path):
        response = requests.get(img_url)
        img_data = response.content
        with open(img_path, "wb") as f:
            f.write(img_data)
        time.sleep(5)
    return img_path


if __name__ == '__main__':
    ahk = AutoHotkey()
    init()
    main()
