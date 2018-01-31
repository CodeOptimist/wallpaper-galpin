import urllib.request
import json
import os
import re
import PIL.ImageOps
from PIL import Image
from collections import OrderedDict
from galpin_27_36.ahk import helper as ahk
import time
import datetime

url = "https://www.reddit.com/r/EarthPorn/top.json?t=day"
minute_interval = 60
data = None


def main():
    monitors, screen = get_monitor_info()

    directory = r"C:\Working\earthporn"
    if not os.path.isdir(directory):
        os.makedirs(directory)

    while True:
        update_json(os.path.join(directory, 'earthporn.json'))
        load_wallpaper(directory, monitors, screen)
        time.sleep(60)


def update_json(path):
    global data
    if os.path.isfile(path):
        age = time.time() - os.path.getmtime(path)
        is_recent_file = age <= minute_interval * 60
        if is_recent_file:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return

        is_time_to_fetch = datetime.datetime.now().time().minute % minute_interval == 0
        if data is not None and not is_time_to_fetch:
            return

    print(datetime.datetime.now(), "fetching JSON")
    req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Python 3.6.1 (Windows NT 10.0):wallpaper-galpin:v1.0 (by /u/CodeOptimist)'})
    with urllib.request.urlopen(req, timeout=5) as response:
        data_str = response.read().decode()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data_str)
        data = json.loads(data_str)


def load_wallpaper(directory, monitors, screen):
    wallpaper = Image.new("RGB", (screen['w'], screen['h']))
    for idx, monitor in monitors.items():
        img_path = get_image(directory, monitor)
        img = Image.open(img_path)
        img = PIL.ImageOps.fit(img, (monitor['w'], monitor['h']), PIL.Image.LANCZOS)
        # img.save(os.path.join(directory, '{}.jpg'.format(idx)))
        wallpaper.paste(img, (monitor['x'] - screen['x'], monitor['y'] - screen['y']))
        # print(idx, monitor['x'], monitor['y'])
    wallpaper_path = os.path.join(directory, 'wallpaper.jpg')
    wallpaper.save(wallpaper_path)
    ahk.execute(r'DllCall("SystemParametersInfo", UInt, 0x14, UInt, 0, Str, "{}", UInt, 2)'.format(wallpaper_path))


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
    SM_CMONITORS = 80
    ahk.execute(r'SysGet, numMon, {}'.format(SM_CMONITORS))
    result['num'] = ahk.get('numMon')

    SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN = (78, 79)
    ahk.execute(r'SysGet, virtualScreenW, {}'.format(SM_CXVIRTUALSCREEN))
    result['w'] = int(ahk.get('virtualScreenW'))
    ahk.execute(r'SysGet, virtualScreenH, {}'.format(SM_CYVIRTUALSCREEN))
    result['h'] = int(ahk.get('virtualScreenH'))

    SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN = (76, 77)
    ahk.execute(r'SysGet, virtualScreenX, {}'.format(SM_XVIRTUALSCREEN))
    result['x'] = int(ahk.get('virtualScreenX'))
    ahk.execute(r'SysGet, virtualScreenY, {}'.format(SM_YVIRTUALSCREEN))
    result['y'] = int(ahk.get('virtualScreenY'))

    return result


def get_image(directory, monitor):
    for img_json in data['data']['children']:
        if 'is_retrieved' in img_json:
            continue

        title = img_json['data']['title']
        m = re.search(r'[\[(]\s*(?P<w>\d+)\s*\D\s*(?P<h>\d+)[)\]]', title)
        if m is None:
            continue

        w = int(m.group('w'))
        h = int(m.group('h'))
        if w < monitor['w'] or h < monitor['h']:
            continue
        is_oriented_same = (monitor['w'] / monitor['h'] > 1) == (w / h > 1)
        if not is_oriented_same:
            continue

        try:
            img_url = img_json['data']['url']
            img_path = get_img(directory, img_url)
        except Exception:
            continue

        img_json['is_retrieved'] = True
        return img_path
    return None


def get_img(directory, img_url):
    img_filename = os.path.basename(img_url)
    img_path = os.path.join(directory, img_filename)
    if not os.path.isfile(img_path):
        with urllib.request.urlopen(img_url) as response:
            img_data = response.read()
        with open(img_path, "wb") as f:
            f.write(img_data)
        print(img_path)
    return img_path


if __name__ == '__main__':
    ahk.start()
    ahk.ready()
    main()
