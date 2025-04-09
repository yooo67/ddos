import socket
import time
import sys
import threading
import subprocess

def tcp_ping(target_ip, target_port, interval=0.5): 
    start_time = time.time()
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(5)
            client_socket.connect((target_ip, target_port))
            client_socket.close()
            end_time = time.time()
            response_time = (end_time - start_time) * 1000
            print(f"\033[97m               Connected to \033[94m{target_ip}\033[97m: \033[97mtime=\033[94m{response_time:.2f}ms \033[97mprotocol=\033[94mTCP \033[97mport=\033[94m{target_port}")
        except Exception as e:
            print("\033[91m                                 Connection timed out")
        
        if time.time() - start_time >= 50:  # Jika sudah 50 detik
            break  # Stop pengulangan

        time.sleep(interval)

    # Menjalankan main.py setelah 50 detik
    threading.Timer(50, run_main).start()

def run_main():
    subprocess.run(["python3", "main.py"])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 paping.py ip port")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    interval = 0.4
    tcp_ping(target_ip, target_port, interval)
