import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nombre = raw_input("Introduce tu nombre: ")

sock.bind(('localhost', 2085))
sock.listen(1)

socket_cliente, addr = sock.accept()

socket_cliente.send(nombre)
nombre_cliente = socket_cliente.recv(1024)

print("-------"+nombre_cliente+" se ha unido-------")

check = True
while check:

    mensaje = socket_cliente.recv(1024)

    if mensaje == "exit":
        check = False
        print(nombre_cliente + " ha salido del chat")
        sock.close()
        socket_cliente.close()

    else:
        print(nombre_cliente + ": " + mensaje)

    enviar = raw_input(nombre+": ")

    if(enviar == "exit"):
        check = False
        socket_cliente.send(nombre+" ha salido del chat")
        sock.close()
        socket_cliente.close()

    else:
        socket_cliente.send(enviar)








