import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nombre = raw_input("Introduce tu Nombre: ")
udp.sendto(nombre,("localhost", 2502))

nombre_server, addr = udp.recvfrom(1024)
print(nombre_server)

check = True
while check:
    message = raw_input(nombre+": ")

    if message == "exit":
        udp.sendto(message, ("localhost", 2502))
        check = False
        print("chat finalizado")
        udp.close()
    else:
        udp.sendto(message, ("localhost", 2502))

    data, addr = udp.recvfrom(1024)

    if data  == "exit":
        check = False
        print("chat finalizado")
        udp.close()
    else:
        print(nombre_server+":"+data)



