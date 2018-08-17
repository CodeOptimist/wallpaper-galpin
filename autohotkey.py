# Copyright (C) 2018  Christopher S. Galpin.  See /NOTICE.
import ctypes, time, re


class AutoHotkey(object):
    def __init__(self, script="#Persistent\n#NoTrayIcon"):
        ctypes.cdll.LoadLibrary(r'lib\msvcr100.dll')
        self._ahk = ctypes.cdll.LoadLibrary(r'lib\AutoHotkey\AutoHotkey.dll')
        self._ahk.ahkTextDll(script, None, None)
        while not self._ahk.ahkReady():
            time.sleep(0.01)

    def _get(self, name):
        self._ahk.ahkGetVar.restype = ctypes.c_int64
        result = self._ahk.ahkGetVar(name, 0)
        result = ctypes.cast(int(result), ctypes.c_wchar_p)
        result = result.value
        if result is not None:
            is_hex = result.startswith('0x') and result[2:].isdigit()
            is_negative = result.startswith('-') and result[1:].isdigit()
            if result.isdigit() or is_hex or is_negative:
                result = int(result, 0)
        return result

    def get(self, name):
        if not name:
            raise ValueError("Variable name wasn't provided")
        if len(name) > 253:
            raise ValueError("Variable name length must be <= 253")
        if not re.fullmatch(r'[\d\w#@$]+', name):
            raise ValueError("Variable names may only consist of letters, numbers and the following punctuation: # _ @ $")

        # the following causes a heap corruption:
        # ahkExec('result = abc') # or ahkAssign('result', 'abc')
        # ahkExec('result = 1234') # ahkAssign('result', '1234') seems safe
        # ahkGetVar('result', 0)
        # ahkGetVar('result', 0)
        # where the second assignment is a number (be it "1234" or 1234) of a longer length than the first assignment

        # we can work around it by copying to a fresh variable before retrieving
        self._ahk.ahkAssign('__get', '') # clear variable or bug can still occur from previous use
        # '= %var%' vs. ':= var' to help enforce a variable name instead of arbitrary code
        self._ahk.ahkExec('__get = %{}%'.format(name))
        return self._get('__get')

    def set(self, name, val):
        self._ahk.ahkAssign(name, val)

    def execute(self, script):
        return self._ahk.ahkExec(script)

    def f(self, script):
        self._ahk.ahkAssign('__f' ,'')
        self._ahk.ahkExec('__f := ' + script)
        return self._get('__f')

    def tooltip(self, text, s):
        if not self.f('IsLabel("RemoveToolTip")'):
            self.execute("""
                RemoveToolTip:
                    SetTimer, RemoveToolTip, Off
                    ToolTip,
                    return
            """)

        self.set('__tooltip', text)
        self.execute("""
            ToolTip, % __tooltip
            SetTimer, RemoveToolTip, {s}
            return
        """.format(s=int(s * 1000)))
