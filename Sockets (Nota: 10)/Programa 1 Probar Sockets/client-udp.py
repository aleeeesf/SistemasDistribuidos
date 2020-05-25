import socket
import time

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


message = raw_input("Envia mensaje: ")
udp.sendto(message,("localhost",1207))
print("Mensaje enviado")

udp.close()


