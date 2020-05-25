import socket
import threading
import time

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nombre = raw_input("Introduce tu Nombre: ")
udp.sendto(nombre,("localhost", 2511))

def recibir():
    check = True
    while check:
        try:
            data, addr = udp.recvfrom(1024)
            if data == "intr_apodo":
                udp.sendto(nombre,addr)
            else:
                print(data)
        except:
            print("IMPORTANTE: NO estas en el chat")
            check = False
            udp.close()

def mostrar():
    check = True
    while check:
        data = raw_input()
        if data == "salir":
            udp.sendto(data,("localhost",2511))
            print("~ Has salido del chat ~")
            udp.close()
            check = False
        else:
            udp.sendto(nombre+": "+data,("localhost",2511))

recibir_thread = threading.Thread(target=recibir)
escribir_thread = threading.Thread(target=mostrar)
recibir_thread.start()
escribir_thread.start()