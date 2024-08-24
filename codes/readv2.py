# python3 readv2.py ../wireshark/capture-icmp.pcapng

from langdetect import detect
from scapy.all import *
import sys
from transformers import pipeline

classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

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


def cesar(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if char == " ":
            result += " "
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isnumeric():
            result += str((int(char) + shift) % 10)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += chr(ord(char) + shift)

    return result            

def es_espanol(texto):
    result = classifier(texto)
    return result[0]['label'] == 'es'

# def es_espanol(texto):
#     try:
#         return detect(texto) == 'es'
#     except:
#         return False
    

# texto = "criptografia y seguridad en redes"
# if es_espanol(texto):
#     print("El texto está en español")
# else:
#     print("El texto no está en español")    


for word in words:
    print(f"Palabra original: {word}")
    shift = 1
    for i in range(len(word)):
        tmp = cesar(word, shift)
        
        if es_espanol(tmp):
            print(f"\033[92m{tmp}\033[0m")  
        else:
            print(f"{tmp}")
        
        shift += 1
    print("\n")