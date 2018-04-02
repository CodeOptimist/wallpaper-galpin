# Copyright (C) 2018  Christopher S. Galpin.  See /NOTICE.
import json, os, re, glob, tempfile, time, platform, sys
from json import JSONDecodeError
from collections import OrderedDict
from datetime import datetime, timedelta

import requests, pytz, tzlocal, click
from _ctypes import COMError
import PIL.ImageOps
from PIL import Image
from comtypes.client import CreateObject

from autohotkey import AutoHotkey
from gen.ShObjIdl_core import IDesktopWallpaper, DWPOS_SPAN


# change this if you've forked the project, at the very least so the User-Agent is different
NAME = 'wallpaper-galpin'
APP_DIR = os.path.join(os.getenv('APPDATA'), NAME)
TMP_DIR = os.path.join(tempfile.gettempdir(), NAME)
SEEN_JSON_PATH = os.path.join(APP_DIR, 'seen.json')
MAX_SEEN = 1000  # about how many images the most popular sees in a week
MAX_PAGE_COUNT = 3
FETCH_RETRY_COUNT = 3
FETCH_RETRY_DELAY_S = 60


def get_version():
    if not getattr(sys, 'frozen', False):
        return 'dev-{}'.format(int(os.path.getmtime(__file__)))

    # noinspection PyUnresolvedReferences
    version_path = os.path.join(sys._MEIPASS, 'version')
    with open(version_path, 'r') as f:
        result = f.readline()
    return result


version = get_version()
has_lf = True


@click.command(name=NAME, context_settings={'terminal_width': 100})
@click.argument('subreddit', default='earthporn')
@click.option('--daemon/--no-daemon', default=True, show_default=True,
              help="Keeps program running to update on an automated schedule."
                   " Otherwise exits immediately after applying a due update. (--FORCE will always update.)")
@click.option('--hours', default=1, show_default=True,
              help="Update interval in hours.")
@click.option('--scale-hours/--no-scale-hours', default=True, show_default=True,
              help="Scale --HOURS with connected monitor count, e.g. every 2 hours when 2 monitors."
                   " Useful as you may quickly exhaust all weekly photos from the subreddit otherwise.")
@click.option('--force/--no-force', default=False, show_default=True,
              help="Force an immediate update, regardless of whether it's due. Then proceeds as scheduled.")
@click.option('--min-fit', default=0.0, show_default=True,
              help="Minimum coverage of original image required after fitting to monitor, e.g. 0.5 for 50%. Might use to exclude panoramas, etc."
                   " Generally unnecessary with the default --ORIENT option as same-oriented panoramas look quite good cropped to center.")
@click.option('--orient/--no-orient', default=True, show_default=True,
              help="Require an image to have the same orientation as monitor."
                   " Although sufficiently large images will fit without this, excessive cropping is often unaesthetic (you can limit with --MIN-FIT)."
                   " --NO-ORIENT may be useful if your subreddit lacks sufficient images of the same orientation.")
@click.option('--forget-accepted', default=False, is_flag=True, show_default=True,
              help="Wipe memory of accepted images so they may reappear (if still in the top weekly).")
@click.option('--forget-rejected', default=False, is_flag=True, show_default=True,
              help="Wipe memory of rejected images so they may be reevaluated against new --MIN-FIT or --ORIENT parameters."
                   " This isn't necessary for monitor resolution changes.")
@click.option('--use-saved/--no-use-saved', default=True, show_default=True,
              help="Immediately applies the previously saved subreddit wallpaper (may be the same) before proceeding as normal.")
@click.version_option(version=version)
def cli(**kwargs):
    """Updates each monitor with wallpaper from SUBREDDIT [default: earthporn] top weekly.

SFWPornNetwork
https://www.reddit.com/r/sfwpornnetwork/wiki/network
"""
    global argv
    argv = kwargs
    init()
    main()


def init():
    global ahk, wallpaper_path
    wallpaper_path = os.path.join(APP_DIR, 'wallpaper-' + argv['subreddit'] + '.png')
    ahk = AutoHotkey()

    try: os.makedirs(APP_DIR)
    except FileExistsError: pass
    try: os.makedirs(TMP_DIR)
    except FileExistsError: pass

    load_seen()

    PROCESS_PER_MONITOR_DPI_AWARE = 0x2
    ahk.execute('DllCall("Shcore.dll\SetProcessDpiAwareness", Int, {})'.format(PROCESS_PER_MONITOR_DPI_AWARE))


def load_seen():
    global seen_json
    seen_json_defaults = {'accepted': [], 'rejected': []}
    try:
        with open(SEEN_JSON_PATH, 'r+') as f:
            seen_json = json.load(f)

            if argv['forget_accepted'] or argv['forget_rejected']:
                if argv['forget_accepted']:
                    seen_json['accepted'].clear()
                if argv['forget_rejected']:
                    # all of 'rejected_N' but not 'rejected'
                    seen_json = {k: v for k, v in seen_json.items() if not k.startswith('rejected_')}
                f.seek(0)
                f.truncate()
                json.dump(seen_json, f)
    except JSONDecodeError:
        log("Couldn't decode 'seen images' file: '{}'. Using blank. Will be overwritten on update.".format(SEEN_JSON_PATH))
        seen_json = seen_json_defaults
    except FileNotFoundError:
        seen_json = seen_json_defaults

    for k, v in seen_json_defaults.items():
        if k not in seen_json:
            seen_json[k] = v


def log(*args):
    global has_lf
    if not has_lf:
        print()
    print('\t', *args)
    has_lf = True


def minute_dt(dt=None, local=False):
    if dt is None:
        dt = datetime.now(pytz.utc)
    elif dt.tzinfo is None:
        dt = dt.replace(tzinfo=pytz.utc)

    dt = dt.replace(second=0, microsecond=0)
    if local:
        dt = dt.astimezone(tzlocal.get_localzone())
    return dt


def main():
    global update_every_m
    print("For proper status messages don't resize this window. Leave running for scheduled updates.")
    last_interval_at = minute_dt(datetime.min) if argv['force'] else get_file_modified_at(SEEN_JSON_PATH)
    just_ran = True

    while True:
        update_monitor_info()
        update_every_m = argv['hours'] * 60 * (len(monitors) if argv['scale_hours'] else 1)
        print_status()

        update_due_at = last_interval_at + timedelta(minutes=update_every_m)
        is_update_due = minute_dt() > update_due_at
        idle_s = ahk.f('A_TimeIdlePhysical') / 1000

        if is_update_due and (just_ran or idle_s <= 60):
            print_status("Update at '{}'".format(minute_dt(local=True)))
            update_wallpaper()
            last_interval_at = minute_dt()
        else:
            if just_ran and argv['use_saved'] and os.path.isfile(wallpaper_path):
                set_wallpaper(wallpaper_path)

            if not argv['daemon']:
                log("exiting")
                sys.exit()

            update_in = update_due_at - minute_dt() + timedelta(minutes=1)
            print_status("Next update in: '{}' at: '{}'".format('Idle' if update_in < timedelta(0) else str(update_in)[:-3].zfill(5), minute_dt(update_due_at, local=True)))
            time.sleep(30)

        just_ran = False


def update_wallpaper():
    global seen_json

    old_tmp = list(glob.glob(os.path.join(TMP_DIR, '*.*'), recursive=False))
    old_accepted = seen_json['accepted'].copy()

    wallpaper = None
    try:
        wallpaper = get_wallpaper()
    except OutpacedError:
        log("Suitable image not found within {} pages. Skipping update."
            " Updates have outpaced the subreddit, you may need a longer time (--HOURS) or relaxed image requirements.".format(MAX_PAGE_COUNT))

    if wallpaper:
        wallpaper.save(wallpaper_path)
        set_wallpaper(wallpaper_path)
        log("stitching wallpaper")
    else:
        seen_json['accepted'] = old_accepted

    with open(SEEN_JSON_PATH, 'w') as f:
        json.dump(seen_json, f)

    for entry in old_tmp:
        try:
            os.remove(entry)
        except OSError:
            pass


def print_status(msg=""):
    global has_lf
    status = "* Monitors: '{}' Update frequency: '{}'".format(len(monitors), str(timedelta(minutes=update_every_m))[:-3].zfill(5))
    status += ' ' + msg
    status += ' ' * (119 - len(status))
    print(status, end='\r', flush=True)
    has_lf = False


def get_file_modified_at(path):
    try:
        timestamp = os.path.getmtime(path)
    except OSError:
        timestamp = 0
    result = minute_dt(datetime.utcfromtimestamp(timestamp))
    return result


def fetch_json(after):
    json_url = "http://www.reddit.com/r/{}/top.json?t=week&limit=100&after={}".format(argv['subreddit'], after)
    log("fetching", json_url)

    for fetch_attempt_num in range(1, FETCH_RETRY_COUNT + 1):
        try:
            response = requests.get(json_url, headers={
                'User-Agent': "{} ({}):{}:{} (by /u/CodeOptimist)".format(sys.version, platform.platform(), NAME, version)
            }, timeout=30)

            sub_json = response.json()

            if not sub_json['data']['children']:
                raise ValueError("'{}' doesn't appear to be a valid subreddit".format(argv['subreddit']))

            return sub_json
        except (ConnectionError, TimeoutError):
            if fetch_attempt_num == FETCH_RETRY_COUNT:
                raise
            time.sleep(FETCH_RETRY_DELAY_S)


def get_wallpaper():
    global seen_json
    sub_json = fetch_json(after="")  # fetch #1

    wallpaper = Image.new("RGB", (screen['w'], screen['h']))
    for idx, monitor in monitors.items():
        rejected_wh = 'rejected_{}_{}'.format(monitor['w'], monitor['h'])
        if rejected_wh not in seen_json:
            seen_json[rejected_wh] = []

        try:
            for _page_fetch_num in range(2, MAX_PAGE_COUNT + 1):
                for img_json in sub_json['data']['children']:
                    img_name = os.path.basename(img_json['data']['url'])
                    already_seen = any(img_name in seen_json[k] for k in ('accepted', 'rejected', rejected_wh))
                    if already_seen:
                        continue

                    try:
                        stitch_wallpaper(img_json, wallpaper, monitor)
                        log(idx, '"{}"'.format(img_json['data']['title']))
                        seen_append('accepted', img_name)
                        raise ImageSuccess
                    except MonitorImageRejectedError:
                        seen_append(rejected_wh, img_name)
                    except ImageRejectedError:
                        seen_append('rejected', img_name)

                sub_json = fetch_json(sub_json['data']['after'])

            raise OutpacedError

        except ImageSuccess:
            continue

    return wallpaper


# can't natively json encode a deque, so we'll use this
def seen_append(name, item):
    lst = seen_json[name]
    if len(lst) == MAX_SEEN:
        lst.pop(0)
    lst.append(item)


def stitch_wallpaper(img_json, wallpaper, monitor):
    img, img_path = get_img(img_json, monitor)
    fit_img = PIL.ImageOps.fit(img, (monitor['w'], monitor['h']), PIL.Image.LANCZOS)
    name, ext = os.path.splitext(os.path.basename(img_path))
    fit_img.save(os.path.join(TMP_DIR, name + '_fit' + '.png'))
    wallpaper.paste(fit_img, (monitor['x'] - screen['x'], monitor['y'] - screen['y']))


def set_wallpaper(path):
    # # doesn't work due to limitation of calling AutoHotkey.dll (uses SendMessage/PostMessage):
    # # "An outgoing call cannot be made since the application is dispatching an input-synchronous call."
    # # Anyone have a solution?
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
    try:
        com_obj.SetWallpaper(None, path)
    except COMError as e:
        log(repr(e))
    com_obj.SetPosition(DWPOS_SPAN)
    com_obj.Release()


def update_monitor_info():
    global screen, monitors
    screen = get_screen_info()
    monitors = OrderedDict()
    for idx in range(1, screen['num'] + 1):
        monitors[idx] = {}
        ahk.execute('SysGet, mon{0}, Monitor, {0}'.format(idx))
        l, t, r, b = [int(ahk.get('mon{}{}'.format(idx, side))) for side in ("Left", "Top", "Right", "Bottom")]

        monitors[idx]['x'] = l
        monitors[idx]['y'] = t
        monitors[idx]['w'] = r - l
        monitors[idx]['h'] = b - t


def get_screen_info():
    result = {}
    SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN, SM_CMONITORS = (76, 77, 78, 79, 80)
    for c, n in zip(('x', 'y', 'w', 'h', 'num'), (SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN, SM_CMONITORS)):
        ahk.execute('SysGet, result, {}'.format(n))
        result[c] = int(ahk.get('result'))
    return result


class ImageSuccess(Exception):
    pass


class ImageRejectedError(Exception):
    pass


class MonitorImageRejectedError(Exception):
    pass


class OutpacedError(Exception):
    pass


def get_img(img_json, monitor):
    img_url = img_json['data']['url']
    if '//imgur.com/' in img_url:
        img_url = img_url.replace('//imgur.com/', '//i.imgur.com/') + '.jpg'
    if not img_url.endswith('.jpg') and not img_url.endswith('.jpeg'):
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
    try:
        img = Image.open(img_path)
    except OSError:
        raise ImageRejectedError
    img.load()  # immediately closes file

    w, h = img.size
    if w < monitor['w'] or h < monitor['h']:
        raise MonitorImageRejectedError

    is_oriented_same = (monitor['w'] / monitor['h'] >= 1) == (w / h >= 1)
    if argv['orient'] and not is_oriented_same:
        raise MonitorImageRejectedError

    img_ar = w / h
    mon_ar = monitor['w'] / monitor['h']
    fit_percent = (mon_ar * h) / w if img_ar >= mon_ar else (w / mon_ar) / h

    is_fit = fit_percent >= argv['min_fit']
    if not is_fit:
        raise MonitorImageRejectedError

    return img, img_path


def fetch_img(img_url):
    img_name = os.path.basename(img_url)
    img_path = os.path.join(TMP_DIR, img_name)

    for fetch_attempt_num in range(1, FETCH_RETRY_COUNT + 1):
        try:
            if not os.path.isfile(img_path):
                response = requests.get(img_url, timeout=30)
                img_data = response.content
                with open(img_path, "wb") as f:
                    f.write(img_data)
            return img_path
        except (ConnectionError, TimeoutError):
            if fetch_attempt_num == FETCH_RETRY_COUNT:
                raise
            time.sleep(FETCH_RETRY_DELAY_S)


if __name__ == '__main__':
    cli()
