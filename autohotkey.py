import ctypes, time

# download to folder (not included due to incompatible license):
# https://github.com/HotKeyIt/ahkdll-v1-release/raw/master/Win32w/AutoHotkey.dll
# https://github.com/HotKeyIt/ahkdll-v1-release/raw/master/Win32w/msvcr100.dll

class AutoHotkey(object):
    def __init__(self):
        self.ahk = ctypes.cdll.LoadLibrary('AutoHotkey.dll')
        self.ahk.ahktextdll(None, None, None)
        while not self.ahk.ahkReady():
            time.sleep(0.01)

    def _get(self, name, is_pointer=False):
        self.ahk.ahkgetvar.restype = ctypes.c_int64
        result = self.ahk.ahkgetvar(name, 0)
        result = ctypes.cast(int(result), ctypes.c_wchar_p)
        if is_pointer:
            return result
        return result.value

    def get(self, name, is_pointer=False):
        result = self._get(name, is_pointer)
        if result is not None:
            if result.startswith('0x') or result.isdigit():
                result = int(result, 0)
        return result

    def execute(self, str):
        return self.ahk.ahkExec(str)

    def f(self, str):
        self.execute('result := ' + str)
        result = self.get('result')
        return result
