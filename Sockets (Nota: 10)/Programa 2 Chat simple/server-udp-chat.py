import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nombre = raw_input("Introduce tu Nombre: ")

udp.bind(("localhost",2502))

nombre_cliente, addr = udp.recvfrom(1024)

udp.sendto(nombre,addr)

check = True
while check:

    data, addr = udp.recvfrom(1024)

    if data == "exit":
        check = False
        print("chat finalizado")
        udp.close()
    else:
        print(nombre_cliente+": "+data)
        message = raw_input(nombre+": ")

        if message == "exit":
            check = False
            udp.sendto("exit",addr)
            udp.close()
        else:
            udp.sendto(message,addr)


