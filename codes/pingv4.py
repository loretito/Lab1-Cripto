# sudo python3 pingv4.py "larycxpajotj h bnpdarmjm nw anmnb"

from scapy.all import *
import sys

# Obtener el mensaje desde la línea de comandos
message = sys.argv[1]

# Crear el paquete ICMP
icmp_packet = IP(dst="8.8.8.8")/ICMP()/message

# Enviar el paquete
send(icmp_packet)
send(icmp_packet)
send(icmp_packet)

# Mostrar el mensaje en la consola
print(f"Mensaje enviado: {message}")
