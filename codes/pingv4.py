from scapy.all import *
import time
import os
import random
import sys

message = sys.argv[1]

def send_data(data):
    for char in data:
        random_size = random.randint(30,47)
        filled = os.urandom(random_size)

        padded_data = char.encode() + filled

        pkt = IP(dst="8.8.8.8")/ICMP()/Raw(load=padded_data)
        send(pkt)

        time.sleep(random.randint(1,2))

send_data(message)        
print("\nMensaje enviado")