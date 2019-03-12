; when included from Python the auto-execution section has already ended, so this is ignored
#NoEnv
#SingleInstance force
Init()

Init() {
    global recent, runHistory, status, comIDesktopWallpaper, comSetWallpaper, comSetPosition

    comIDesktopWallpaper := ComObjCreate("{C2CF3110-460E-4fc1-B9D0-8A1C0C9CC4BD}", "{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}")
    vTbl := NumGet(comIDesktopWallpaper + 0, 0, "Ptr")
    comSetWallpaper := NumGet(vTbl + 0, 3 * A_PtrSize, "Ptr")
    comSetPosition := NumGet(vTbl + 0, 10 * A_PtrSize, "Ptr")

    Menu, FileMenu, Add, E&xit, Exit
    Menu, HelpMenu, Add, &About, About
    Menu, MyMenuBar, Add, &File, :FileMenu
    Menu, MyMenuBar, Add, &Help, :HelpMenu

    Menu, Tray, Icon, lib\\black.ico
    Menu, Tray, Icon
    Menu, Tray, Tip, {{NAME}} {{version}}
    Menu, Tray, NoStandard
    Menu, Tray, Add, Open, Restore
    Menu, Tray, Default, Open
    Menu, Tray, Click, 1
    Menu, Tray, Add, Exit, Exit

    Gui, StringWidth:Font,, Consolas
    Gui, StringWidth:Add, Text,, WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    GuiControlGet, t, StringWidth:Pos, Static1
    Gui, StringWidth:Destroy

    Gui, MyGui:New, +LabelMyGui +HwndMyGuiHwnd, {{NAME}} {{version}}
    Gui, Menu, MyMenuBar
    Gui, Font,, Consolas
	Gui, Add, Tab3,, Recent|Run History
    Gui, Add, Link, % "w" tW " r20 vRecent"
	Gui, Tab, Run History
    Gui, Add, Edit, % "w" tW " r20 vRunHistory ReadOnly -Wrap HScroll"
	Gui, Tab
	Gui, Add, Text,, Status
    Gui, Add, Edit, % "w" tW+24 " vStatus ReadOnly"
    Gui, Show, AutoSize
}

Restore:
    Gui, MyGui:+LastFound
    WinShow
    WinRestore
return

Exit:
    ObjRelease(comIDesktopWallpaper)
    ExitApp
return

HideConsole(pid) {
    global console, isHid
    console := pid
    WinHide, ahk_pid %pid%
    isHid := true

    Menu, WindowMenu, Add, &Console, Console
    Menu, MyMenuBar, Insert, &Help, &Window, :WindowMenu
}

Console:
    if (not console)
        return

    if (isHid)
        WinShow, ahk_pid %console%
    else
        WinHide, ahk_pid %console%
    isHid := not isHid
    Menu, WindowMenu, ToggleCheck, &Console
return

About() {
    Gui, MyGui:+Disabled
    Gui, About:New, +OwnerMyGui -MaximizeBox -MinimizeBox +LabelAbout +HwndAboutHwnd, About

    link =
    ( LTrim
        Multi-Monitor Reddit Wallpaper

        Copyright (C) 2018  Christopher Galpin

        <a href="https://github.com/CodeOptimist/multimonitor-reddit-wallpaper">Multi-Monitor Reddit Wallpaper</a>
        <a href="https://github.com/CodeOptimist/python-autohotkey-bidirectional">Python ↔ AutoHotkey</a>
    )
    Gui, Add, Link,, % link
    Gui, Show, w300 h100
}

AboutClose(GuiHwnd) {
    Gui, MyGui:-Disabled
}

MyGuiClose(GuiHwnd) {
    WinHide
}

MyGuiSize(GuiHwnd, EventInfo, Width, Height) {
    isMinimize := EventInfo = 1
    if (isMinimize)
        WinHide
}

GuiText(name, val) {
	local new
	new := val
	%name% := new
	GuiControl, MyGui:, %name%, %new%
}

GuiTextAppend(name, val) {
	local new
	new := %name% val "`n"
	%name% := new
	GuiControl, MyGui:, %name%, %new%
}

StoreMousePos() {
    global x, y
    CoordMode, Mouse, Screen
    MouseGetPos, x, y
}

StoreSysGetMonitors(idx) {
    global
    SysGet, mon%idx%, Monitor, % idx
}

StoreSysGet(n) {
    global result
    SysGet, result, % n
}

SetWallpaper(path) {
    global comIDesktopWallpaper, comSetWallpaper, comSetPosition
    DllCall(comSetWallpaper, "Ptr", comIDesktopWallpaper, "Str", "", "Str", path)
    DWPOS_SPAN := 5
    DllCall(comSetPosition, "Ptr", comIDesktopWallpaper, "Int", DWPOS_SPAN)
}

#IfWinActive ahk_class Progman
~MButton::
^LButton::
#IfWinActive ahk_class WorkerW
~MButton::
^LButton::
    pressed_hotkey = {{Hotkey.DESCRIPTION}}
return
