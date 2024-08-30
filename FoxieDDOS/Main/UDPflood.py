from scapy.all import IP, UDP, send
import os
import random
import socket
import threading
import time
import datetime # digunakan untuk mendapatkan waktu realtime saat mengukur suatu operasi

def udp_banner():
    RESET = '\033[0m'
    BIRU = '\033[0;34m'

    os.system("clear")

    print("\n")

    print(f"""{BIRU}

          ______   _______    _______  _        _______  _______  ______  
|\     /|(  __  \ (  ____ )  (  ____ \( \      (  ___  )(  ___  )(  __  \ 
| )   ( || (  \  )| (    )|  | (    \/| (      | (   ) || (   ) || (  \  )
| |   | || |   ) || (____)|  | (__    | |      | |   | || |   | || |   ) |
| |   | || |   | ||  _____)  |  __)   | |      | |   | || |   | || |   | |
| |   | || |   ) || (        | (      | |      | |   | || |   | || |   ) |
| (___) || (__/  )| )        | )      | (____/\| (___) || (___) || (__/  )
(_______)(______/ |/         |/       (_______/(_______)(_______)(______/ 
                                                                            
                                                                                                                                                                                                                                                                                                                                                           
        {RESET}""")