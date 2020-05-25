import socket
import threading

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind(("localhost",2511))

clientes = []
apodos = []
direccion = []

def annadir_clientes():
    while True:
        socket_cliente, dir = udp.recvfrom(1024)
        udp.sendto("intr_apodo",dir)
        nick, addr = udp.recvfrom(1024)
        if dir==addr and nick==socket_cliente:
            direccion.append(addr)
            apodos.append(nick)
            clientes.append(socket_cliente)
            enviar_a_todos(nick+" se ha unido al chat\n")
            print("~ "+nick+" se ha unido al chat ~")
            udp.sendto("Te has unido al chat",addr)

            thread = threading.Thread(target=recibir, args=(socket_cliente,))
            thread.start()


def recibir(cliente):
    check = True
    while check:
        try:
            data,addr = udp.recvfrom(1024)

            if data == "salir":
               indice = clientes.index(cliente)
               apodo_indice = apodos[indice]
               eliminar_cliente(cliente)
               enviar_a_todos(apodo_indice + " ha salido del chat")
               print("~"+apodo_indice + " ha salido del chat~")
               check = False
            else:
               enviar_a_todos(data)

        except:
            udp.close()
            check = False


def enviar_a_todos(mensaje):
    for i in direccion:
        udp.sendto(mensaje,i)

def eliminar_cliente(cliente):
    indice = clientes.index(cliente)
    apodo_indice = apodos[indice]
    apodos.remove(apodo_indice)
    clientes.remove(cliente)


annadir_clientes()
