import socket
import time

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("localhost",1207))

data, addr = udp.recvfrom(1024)
print(data)

udp.close()


