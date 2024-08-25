# python3 readv2.py ../wireshark/capture-icmp.pcapng

import sys
from scapy.all import *
from test import evaluate_consistency
from cesar import cesar

if len(sys.argv) < 2:
    print("Uso: python3 leer_icmp.py <archivo.pcapng>")
    sys.exit(1)

archivo_pcapng = sys.argv[1]
paquetes = rdpcap(archivo_pcapng)

words = []

for paquete in paquetes:
    if ICMP in paquete:
        if Raw in paquete:  
            data = paquete[Raw].load
            word = data.decode('utf-8', errors='ignore')
            words.append(word)
            print(f"Datos ICMP recibidos: {word}")
          

for word in words:
    print(f"Palabra original: {word}")
    shift = 1
    for i in range(len(word)):
        tmp = cesar(word, shift)

        if evaluate_consistency(tmp):
            print(f"\033[92m{tmp}\033[0m")  
        else:
            print(f"{tmp}")
        
        shift += 1
    print("\n")