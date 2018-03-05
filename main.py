import requests
import json
import os
import re
import PIL.ImageOps
import math
from PIL import Image
from collections import OrderedDict
import time
import datetime
import glob
import tempfile
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
minute_interval = 60 * 1


def main():
    global app_json, after, minute_interval
    monitors, screen = get_monitor_info()
    minute_interval = 60 * len(monitors)

    if not os.path.isdir(app_dir):
        os.makedirs(app_dir)
    if not os.path.isdir(tmp_dir):
        os.makedirs(tmp_dir)

    if os.path.isfile(app_json_path):
        with open(app_json_path, 'r') as f:
            app_json = json.load(f)
    else:
        app_json = {'accepts': [], 'rejects': []}

    while True:
        if update_json():
            old_tmp = list(glob.glob(os.path.join(tmp_dir, '*.*'), recursive=False))
            if load_wallpaper(monitors, screen):
                after = ""
            with open(app_json_path, 'w') as f:
                json.dump(app_json, f, sort_keys=True, indent=4)
            for entry in old_tmp:
                if os.path.isfile(entry):
                    os.remove(entry)
        time.sleep(60)


def update_json():
    global sub_json
    if os.path.isfile(sub_json_path):
        age = time.time() - os.path.getmtime(sub_json_path)
        is_recent_file = age <= minute_interval * 60
        if is_recent_file:
            with open(sub_json_path, 'r') as f:
                sub_json = json.load(f)
            return False

    is_time_to_fetch = datetime.datetime.now().time().minute % math.gcd(minute_interval, 60) == 0
    if sub_json is not None and not is_time_to_fetch:
        return False

    if ahk.f('A_TimeIdlePhysical') / 1000 / 60 >= minute_interval:
        return False

    return fetch_json()


def fetch_json():
    global sub_json
    json_url = "{}&after={}".format(url, after)
    print(datetime.datetime.now(), "fetching", json_url)
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
        mon_rejects = 'rejects_{}_{}'.format(monitor['w'], monitor['h'])
        if mon_rejects not in app_json:
            app_json[mon_rejects] = []

        try:
            for _json_attempt_idx in range(2):
                for img_json in sub_json['data']['children']:
                    img_name = os.path.basename(img_json['data']['url'])
                    already_seen = any(img_name in app_json[k] for k in ('accepts', 'rejects', mon_rejects))
                    if already_seen:
                        continue

                    try:
                        img, img_path = get_img(img_json, monitor)
                        fit_img = PIL.ImageOps.fit(img, (monitor['w'], monitor['h']), PIL.Image.LANCZOS)
                        name, ext = os.path.splitext(os.path.basename(img_path))
                        fit_img.save(os.path.join(tmp_dir, name + '_fit' + '.png'))
                        print(datetime.datetime.now(), "found", idx, os.path.basename(img_path), img_json['data']['title'])
                        wallpaper.paste(fit_img, (monitor['x'] - screen['x'], monitor['y'] - screen['y']))
                        # print(idx, monitor['x'], monitor['y'])
                        app_json['accepts'].append(img_name)
                        raise ImageSuccess
                    except MonitorImageRejectedError:
                        app_json[mon_rejects].append(img_name)
                    except ImageRejectedError:
                        app_json['rejects'].append(img_name)
                after = sub_json['data']['after']
                fetch_json()
        except ImageSuccess:
            continue
        return False

    wallpaper_path = os.path.join(app_dir, 'wallpaper.png')
    wallpaper.save(wallpaper_path)

    set_wallpaper(wallpaper_path)
    # print(datetime.datetime.now(), "loaded")
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

        MONITOR_DEFAULTTONEAREST = 0x2
        h_monitor = ahk.f('DllCall("MonitorFromPoint", Int, {}, Int, {}, UInt, {})'.format(l, t, MONITOR_DEFAULTTONEAREST))
        ahk.execute(r'DllCall("Shcore.dll\GetScaleFactorForMonitor", Ptr, {}, "UInt *", scaleFactor)'.format(h_monitor))
        scale = ahk.get('scaleFactor') / 100

        monitors[idx]['x'] = l
        monitors[idx]['y'] = t
        monitors[idx]['w'] = int((r - l) * scale)
        monitors[idx]['h'] = int((b - t) * scale)
    print(monitors)
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

    if m is not None:
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
    main()
