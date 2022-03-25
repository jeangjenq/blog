from distutils.spawn import find_executable
import platform
import os

def isNot_exec(name):
    #check whether terminal program exists
    return find_executable(name) is None

def findTerminal():
    termList = ["x-terminal-emulator", "konsole", "gnome-terminal", "urxvt", "rxvt", "termit", "terminator", "Eterm", "aterm", "uxterm", "xterm", "roxterm", "xfce4-terminal", "termite", "lxterminal", "mate-terminal", "terminology", "st", "qterminal", "lilyterm", "tilix", "terminix", "kitty", "guake", "tilda", "alacritty", "hyper"]
    #list taken from https://github.com/i3/i3/blob/next/i3-sensible-terminal
    i = 0
    for term in termList:
        if isNot_exec(term):
            i += 1
        else:
            break
    return termList[i]


if platform.system() == "Windows":
    startCMD = "start cmd /k " + '"' + args + '"'  # Quote unquote in case both paths have spaces
elif platform.system() == "Linux":
    startCMD = findTerminal() + " -e " + args + ' && read line'  # Quote unquote in case both paths have spaces
os.popen(startCMD)