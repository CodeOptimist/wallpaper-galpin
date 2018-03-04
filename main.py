import urllib.request
import json
import os
import re
import PIL.ImageOps
import math
from PIL import Image
from collections import OrderedDict
from galpin_27_36.ahk import helper as ahk
import time
import datetime
import pickle
import glob

url = "http://www.reddit.com/r/EarthPorn/top.json?t=week&limit=100"
after = ""
minute_interval = 60 * 4
required_fit_percent = 0.00
app_dir = r"C:\Working\earthporn"
tmp_dir = os.path.join(app_dir, 'tmp')
json_path = os.path.join(app_dir, 'earthporn.json')
app_data = None
json_data = None


def main():
    global app_data, after
    monitors, screen = get_monitor_info()

    if not os.path.isdir(app_dir):
        os.makedirs(app_dir)
    if not os.path.isdir(tmp_dir):
        os.makedirs(tmp_dir)

    data_path = os.path.join(app_dir, 'data.bin')
    if os.path.isfile(data_path):
        with open(data_path, 'rb') as f:
            app_data = pickle.load(f)
    else:
        app_data = {'accepts': set(), 'rejects': set()}

    while True:
        if update_json():
            for entry in glob.glob(os.path.join(tmp_dir, '*.*'), recursive=False):
                if os.path.isfile(entry):
                    os.remove(entry)
            if load_wallpaper(monitors, screen):
                after = ""
            with open(data_path, 'wb') as f:
                pickle.dump(app_data, f)
        time.sleep(60)


def update_json():
    global json_data
    if os.path.isfile(json_path):
        age = time.time() - os.path.getmtime(json_path)
        is_recent_file = age <= minute_interval * 60
        if is_recent_file:
            with open(json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            return False

    is_time_to_fetch = datetime.datetime.now().time().minute % math.gcd(minute_interval, 60) == 0
    if json_data is not None and not is_time_to_fetch:
        return False

    if ahk.f('A_TimeIdlePhysical') / 1000 / 60 >= minute_interval:
        return False

    return fetch_json()


def fetch_json():
    global json_data
    json_url = "{}&after={}".format(url, after)
    print(datetime.datetime.now(), "fetching", json_url)
    req = urllib.request.Request(json_url, headers={'User-Agent': 'Python 3.6.1 (Windows NT 10.0):wallpaper-galpin:v2.0 (by /u/CodeOptimist)'})
    with urllib.request.urlopen(req, timeout=5) as response:
        try:
            data_str = response.read().decode()
        except Exception:
            time.sleep(60 * 3)
            return False
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(data_str)
        json_data = json.loads(data_str)
    return True


def load_wallpaper(monitors, screen):
    global after
    wallpaper = Image.new("RGB", (screen['w'], screen['h']))
    for idx, monitor in monitors.items():
        mon_rejects = 'rejects_{}_{}'.format(monitor['w'], monitor['h'])
        if mon_rejects not in app_data:
            app_data[mon_rejects] = set()

        try:
            for _json_attempt_idx in range(2):
                for img_json in json_data['data']['children']:
                    img_name = os.path.basename(img_json['data']['url'])
                    if img_name in app_data['accepts'] | app_data['rejects'] | app_data[mon_rejects]:
                        continue

                    try:
                        img, img_path = get_img(img_json, monitor)
                        fit_img = PIL.ImageOps.fit(img, (monitor['w'], monitor['h']), PIL.Image.LANCZOS)
                        name, ext = os.path.splitext(os.path.basename(img_path))
                        fit_img.save(os.path.join(tmp_dir, name + '_fit' + ext))
                        print(datetime.datetime.now(), "found", idx, os.path.basename(img_path), img_json['data']['title'])
                        wallpaper.paste(fit_img, (monitor['x'] - screen['x'], monitor['y'] - screen['y']))
                        # print(idx, monitor['x'], monitor['y'])
                        app_data['accepts'].add(img_name)
                        raise ImageSuccessError
                    except MonitorImageRejectedError:
                        app_data[mon_rejects].add(img_name)
                    except ImageRejectedError:
                        app_data['rejects'].add(img_name)
                after = json_data['data']['after']
                fetch_json()
        except ImageSuccessError:
            continue
        return False

    wallpaper_path = os.path.join(app_dir, 'wallpaper.jpg')
    wallpaper.save(wallpaper_path)
    ahk.execute(r'DllCall("SystemParametersInfo", UInt, 0x14, UInt, 0, Str, "{}", UInt, 2)'.format(wallpaper_path))
    # print(datetime.datetime.now(), "loaded")
    return True


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


class ImageSuccessError(Exception):
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
    if os.path.isfile(img_path):
        age = time.time() - os.path.getmtime(img_path)
        is_old_file = age > minute_interval * 60
        if is_old_file:
            raise FileExistsError
    else:
        with urllib.request.urlopen(img_url) as response:
            img_data = response.read()
        with open(img_path, "wb") as f:
            f.write(img_data)
        time.sleep(5)
    return img_path


if __name__ == '__main__':
    ahk.start()
    ahk.ready()
    main()
