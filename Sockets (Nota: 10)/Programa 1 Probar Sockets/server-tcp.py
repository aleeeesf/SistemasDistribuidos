import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 2058))
sock.listen(1)

socket_cliente, addr = sock.accept()

mensaje = socket_cliente.recv(1024)
print(mensaje)

sock.close()
socket_cliente.close()




