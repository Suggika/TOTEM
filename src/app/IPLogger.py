
import requests
import sys
import os
import random
from pystyle import *

os.system("cls")

os.system(f'title IPLOGGER FOR TOTEM')


banner = '''
██╗██████╗ ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║██╔══██╗██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██████╔╝██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║██╔═══╝ ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║██║     ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝

                    
       ╔══════════════════════════════════════════════╗
       ║                FOR TOTEM                     ║
       ║              Developer: Suggika              ║
       ║     СДЕЛАТЬ ССЫЛКУ: https://grabify.link/    ║
       ╚══════════════════════════════════════════════╝               
'''

print(Colorate.Horizontal(Colors.white_to_green, Center.XCenter(banner)))
url = input('[>] Привет! Введи свою ссылку с GRABIFY:')
print()
Write.Print("[>] Собираем информацию . . . ", Colors.white_to_green, interval=0.07)
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'} 
response= requests.get(url.strip(), headers=headers, timeout=5)
print()
Write.Print("[!] IP успешно зафиксирован! Проверяй на GRABIFY.", Colors.white_to_green, interval=0.04,)
print()
input()
