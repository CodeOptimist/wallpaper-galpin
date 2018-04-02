# -*- mode: python -*-
import re, time, os

version_path = r'build\version'


class BuildVersionError(Exception):
    pass


def write_version():
    try:
        with open(version_path, 'r') as f:
            version = f.readline().strip()
    except FileNotFoundError as e:
        raise BuildVersionError("Please supply version parameter to build.cmd".format(version_path)) from e

    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise BuildVersionError("Contents of path '{}' don't match format 'N.N.N'\n"
                                "\tPlease supply version parameter to build.cmd".format(version_path))

    ver_w_timestamp = "{}.{:.0f}".format(version, time.time())
    print("Version", ver_w_timestamp)

    with open(version_path, 'w') as f:
        f.write(ver_w_timestamp)


try:
    write_version()

    block_cipher = None


    a = Analysis(['main.py'],
                 pathex=['C:\\Dropbox\\Python\\wallpaper-galpin'],
                 binaries=[],
                 datas=[
                     ('lib', 'lib'),
                     (version_path, r'.')],
                 hiddenimports=[],
                 hookspath=[],
                 runtime_hooks=[],
                 excludes=[],
                 win_no_prefer_redirects=False,
                 win_private_assemblies=False,
                 cipher=block_cipher)
    pyz = PYZ(a.pure, a.zipped_data,
                 cipher=block_cipher)
    exe = EXE(pyz,
              a.scripts,
              a.binaries,
              a.zipfiles,
              a.datas,
              name='wallpaper-galpin',
              debug=False,
              strip=False,
              upx=True,
              runtime_tmpdir=None,
              console=True)
finally:
    try: os.remove(version_path)
    except: pass
