from scapy.all import IP, ICMP, send, Raw
import time
import os
import random
import sys

message = sys.argv[1]

def send_data(data):
    for idx, char in enumerate(data):
        timestamp = int(time.time())
        reversed_bytes = timestamp.to_bytes(8, 'little')

        base_data = bytes(f'{char}\x00\x00', 'utf-8')
        base_data += os.urandom(5) + bytes(range(0x10, 0x38))
        
        payload = reversed_bytes + base_data

        pkt = IP(dst="8.8.8.8")/ICMP(seq=idx, id=random.randint(0, 65535))/Raw(load=payload)

        send(pkt)

        time.sleep(random.uniform(0.5, 2.0))

send_data(message)        
print("\nMensaje enviado")