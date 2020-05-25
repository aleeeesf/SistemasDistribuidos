import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2058))

s.send("Hola mundo!")

mensaje = s.recv(1024)
print(mensaje)
s.close()





