import sys
from scapy.all import ICMP, rdpcap, Raw, IP
from functions import evaluate_consistency, cesar

if len(sys.argv) < 2:
    sys.exit(1)

file_pcapng = sys.argv[1]
packages = rdpcap(file_pcapng)

phrase = ""

for package in packages:
    if ICMP in package and package[IP].dst == "8.8.8.8":
        if Raw in package:  
            data = package[Raw].load
            word = data.decode('utf-8', errors='ignore')
            if word:  # Verifica que no esté vacío
                first_letter = word[0]
                phrase+= first_letter
          
print(f"0: \t{phrase}")

for i in range(len(phrase)):
    tmp = cesar(phrase, i+1, False)

    if evaluate_consistency(tmp):
        print(f"\033[92m{i+1}:\t{tmp}\033[0m")  
    else:
        print(f"{i+1}:\t{tmp}")