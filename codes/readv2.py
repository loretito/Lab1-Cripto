import sys
from scapy.all import *
from functions import evaluate_consistency, cesar

if len(sys.argv) < 2:
    print("Uso: python3 leer_icmp.py <archivo.pcapng>")
    sys.exit(1)

archivo_pcapng = sys.argv[1]
paquetes = rdpcap(archivo_pcapng)

words = ""

for paquete in paquetes:
    if ICMP in paquete and paquete[IP].dst == "8.8.8.8":
        if Raw in paquete:  
            data = paquete[Raw].load
            word = data.decode('utf-8', errors='ignore')
            if word:  # Verifica que no esté vacío
                first_letter = word[0]
                words+= first_letter
          
print(f"0: \t{words}")

for i in range(len(words)):
    tmp = cesar(words, i+1, False)

    if evaluate_consistency(tmp):
        print(f"\033[92m{i+1}:\t{tmp}\033[0m")  
    else:
        print(f"{i+1}:\t{tmp}")