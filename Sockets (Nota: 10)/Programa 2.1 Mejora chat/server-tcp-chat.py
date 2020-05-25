import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost',1047))
sock.listen(1)

clientes = []
apodos = []


def aceptar_clientes():
    while True:
        socket_cliente, addr = sock.accept()
        socket_cliente.send("intr_apodo")
        nick = socket_cliente.recv(1024)
        apodos.append(nick)
        clientes.append(socket_cliente)
        enviar_a_todos(nick+" se ha unido al chat\n")
        print("~ "+nick+" se ha unido al chat ~")
        socket_cliente.send("Te has unido al chat")

        thread = threading.Thread(target=recibir, args=(socket_cliente,))
        thread.start()


def recibir(cliente):
    check = True
    while check:
        try:
            data = cliente.recv(1024)

            if data == "salir":
               indice = clientes.index(cliente)
               apodo_indice = apodos[indice]
               eliminar_cliente(cliente)
               enviar_a_todos(apodo_indice + " ha salido del chat")
               print("~"+apodo_indice + " ha salido del chat~")
               cliente.close()
               check = False
            else:
               enviar_a_todos(data)

        except:
            cliente.close()
            check = False


def enviar_a_todos(mensaje):
    for i in clientes:
        i.send(mensaje)

def eliminar_cliente(cliente):
    indice = clientes.index(cliente)
    apodo_indice = apodos[indice]
    apodos.remove(apodo_indice)
    clientes.remove(cliente)
    cliente.close()


aceptar_clientes()





