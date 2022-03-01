from modules import BannerModule, MenuModule
from colorama import Fore

BannerModule.Banner()


def start_prompt():
    prompt = input(Fore.LIGHTYELLOW_EX + "Black-Android:/# ").lower()

    # check command

    if prompt == "help":
        BannerModule.Banner()
        MenuModule.help()

    elif prompt == "init":
        BannerModule.Banner()
        MenuModule.init()

    elif prompt == "connect":
        BannerModule.Banner()
        MenuModule.connect()

    elif prompt == "device_list":
        BannerModule.Banner()
        MenuModule.device_list()
    
    elif prompt == "disconnect":
        BannerModule.Banner()
        MenuModule.disconnect()

    elif prompt == "shell":
        BannerModule.Banner()
        MenuModule.shell()

    elif prompt == "file_download":
        BannerModule.Banner()
        MenuModule.file_download()

    elif prompt == "file_upload":
        BannerModule.Banner()
        MenuModule.file_upload()

    elif prompt == "file_remove":
        BannerModule.Banner()
        MenuModule.file_remove()

    elif prompt == "screen_shot":
        BannerModule.Banner()
        MenuModule.screen_shot()

    elif prompt == "screen_share":
        BannerModule.Banner()
        MenuModule.screen_share()

    elif prompt == "cam_video":
        BannerModule.Banner()
        MenuModule.open_camera("vidoe")

    elif prompt == "cam_image":
        BannerModule.Banner()
        MenuModule.open_camera("image")


    elif prompt == "open_url":
        BannerModule.Banner()
        MenuModule.open_url()

    elif prompt == "open_video":
        BannerModule.Banner()
        MenuModule.open_video()

    elif prompt == "open_audio":
        BannerModule.Banner()
        MenuModule.open_audio()

    elif prompt == "open_image":
        BannerModule.Banner()
        MenuModule.open_image()

    elif prompt == "remove_app":
        BannerModule.Banner()
        MenuModule.remove_app()

    elif prompt == "install_app":
        BannerModule.Banner()
        MenuModule.install_app()

    elif prompt == "app_list":
        BannerModule.Banner()
        MenuModule.app_list()

    elif prompt == "run_app":
        BannerModule.Banner()
        MenuModule.run_app()
    
    elif prompt == "close_app":
        BannerModule.Banner()
        MenuModule.close_app()


    elif prompt[0:8] == "type_key":
        MenuModule.type_key(prompt[8:])

    elif prompt[0:12] == "touch_screen":
        MenuModule.touch_screen(prompt[12:])

    elif prompt == "call":
        BannerModule.Banner()
        MenuModule.call()

    elif prompt == "sms":
        BannerModule.Banner()
        MenuModule.sms()

    elif prompt == "help":
        BannerModule.Banner()
        MenuModule.help()

    elif prompt == "clear":
        BannerModule.Banner()

    elif prompt == "exit":
        BannerModule.Banner()
        MenuModule.quit_script()

    elif prompt == "shutdown":
        BannerModule.Banner()
        MenuModule.shutdown()

    elif prompt == "reboot":
        BannerModule.Banner()
        MenuModule.reboot()

    elif prompt == "":
        pass

    else:
        print(Fore.GREEN + "[-] " + Fore.RED + "Not Found Command And TRY!")

while True:
    try:
        start_prompt()
    except:
        MenuModule.quit_script()