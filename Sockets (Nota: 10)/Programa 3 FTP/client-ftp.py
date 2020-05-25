import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nombre = raw_input("Introduce tu nombre: ")

s.connect(('localhost', 1055))

#Enviamos nuestro nombre al servidor
s.send(nombre)

#Recibimos un listado de ficheros del directorio del servidor
server_message = s.recv(1024)
print(server_message)

check = True
while check != False:

    command = raw_input("Comando: ")
    s.send(command)

    if command == "list":
        server_message = s.recv(1024)
        print(server_message)

    elif command == "exit":
        server_message = s.recv(1024)
        print(server_message)
        check = False
        
    elif command == "subir":
        confirmacion = s.recv(1024)
        print("Archivo txt desea subir: ")
        command =raw_input()
        s.send(command)
        confirmacion=s.recv(1024)
        file = open(command, 'rb')
        data_file = file.read(1024)
        s.send(data_file)

    else:
        server_message = s.recv(1024)
        if server_message=="error":
            print("el archivo solicitado no existe")
        else:
            os.system("touch " +command)
            file = open(command, 'wb')
            file.write(server_message)
            file.close()

s.close()



