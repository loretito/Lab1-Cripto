# python3 readv2.py ../wireshark/capture-icmp.pcapng
# filter icmp && ip.dst == 8.8.8.8 && ip.src ==
from scapy.all import *
import sys

# Asegurarse de que se ha proporcionado un archivo pcapng
if len(sys.argv) < 2:
    print("Uso: python3 leer_icmp.py <archivo.pcapng>")
    sys.exit(1)

# Cargar el archivo pcapng
archivo_pcapng = sys.argv[1]
paquetes = rdpcap(archivo_pcapng)

words = []

# Recorrer los paquetes y procesar solo los que son ICMP
for paquete in paquetes:
    if ICMP in paquete:
        if Raw in paquete:  # Si el paquete ICMP tiene carga útil (data)
            data = paquete[Raw].load
            words.append(data.decode('utf-8', errors='ignore'))
            print(f"Datos ICMP recibidos: {data.decode('utf-8', errors='ignore')}")


for word in words:
    print(word)
    shift = 1
    for i in range(len(word)): 
        char = word[i]
        if (char == " "):
            word += " "
        elif (char.isupper()):
            word += chr((ord(char) + shift-65) % 26 + 65)
        elif (char.isnumeric()):
            word += str((int(char) + shift) % 10)    
        elif (char.islower()):
            word += chr((ord(char) + shift - 97) % 26 + 97)        
        else:
            word += chr(ord(char)+shift)        
