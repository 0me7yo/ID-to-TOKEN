import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
                  ██████     ██    ██   ████████ ██████████   ██    ██
                ██      ██ ██  █  █  ██ ██           ██     ██  █  █  ██ 
                ████    ██ ██   ██   ██ ██           ██     ██   ██   ██
                ██  ██  ██ ██        ██ ██████       ██     ██        ██
                ██    ████ ██        ██ ██           ██     ██        ██  discord help : https://discord.gg/vCJrak8gXH
                ██      ██ ██        ██ ██           ██     ██        ██
                  ██████   ██        ██ ████████     ██     ██        ██   
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [ENTRE] USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] PREMIERE PARTIE DU TOKEN  : {encodedStr}')
os.system('pause >nul')  
