import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nombre = raw_input("Introduce tu nombre: ")

s.connect(('localhost', 1047))
time.sleep(1)

def recibir():
    check = True
    while check:
        try:
            data = s.recv(1024)
            if data == "intr_apodo":
                s.send(nombre)
            else:
                print(data)
        except:
            print("IMPORTANTE: NO estas en el chat")
            check = False
            s.close()

def mostrar():
    check = True
    while check:
        data = raw_input()
        if data == "salir":
            s.send(data)
            print("~ Has salido del chat ~")
            s.close()
            check = False
        else:
            s.send(nombre+": "+data)

recibir_thread = threading.Thread(target=recibir)
escribir_thread = threading.Thread(target=mostrar)
recibir_thread.start()
escribir_thread.start()



