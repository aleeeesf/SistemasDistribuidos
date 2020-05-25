import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nombre = raw_input("Introduce tu nombre: ")

s.connect(('localhost', 2085))
time.sleep(1)

server_name = s.recv(1024)
s.send(nombre)

check = True
while check:

    message = raw_input(nombre+" : ")

    if message == "exit":
        check = False
        s.send(nombre+" ha salido del chat")
        s.close()

    else:
        s.send(message)

    server_message = s.recv(1024)

    if server_message == "exit":
        check = False
        print(server_name+ " ha salido del chat")
        s.close()

    else:
        print(server_name+": "+server_message)









