import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Estamos a la espera hasta que se establezca conexion
sock.bind(('localhost', 1055))
sock.listen(1)

socket_cliente, addr = sock.accept()
#Recibimos el nombre del cliente
nombre_cliente = socket_cliente.recv(1024)

print("-------"+nombre_cliente+" se ha conectado-------")

#Guardamos en un fichero el listado de los ficheros del directorio.
#Si el fichero no existe crea uno nuevo, o lo sobreescribe.
os.system("ls > list.txt")
file = open("list.txt",'rb')
data_file = file.read(1024)

#Enviamos al cliente el listado de los ficheros
socket_cliente.send(data_file)

check = True
while check != False:

    mensaje = socket_cliente.recv(1024)
    print("El usuario "+nombre_cliente+" ha realizado el siguiente comando: "+mensaje)

    if mensaje == "list":
        os.system("ls > list.txt")
        file = open("list.txt", 'rb')
        data_file = file.read(1024)
        file.close()
        socket_cliente.send(data_file)

    elif mensaje == "exit":
        socket_cliente.send("Sesion finalizada")
        check = False

    elif mensaje == "subir":
        socket_cliente.send("recibido")
        mensaje=socket_cliente.recv(1024)
        socket_cliente.send("recibido")
        os.system("touch " +mensaje)
        os.system("ls > list.txt")
        cliente_message = socket_cliente.recv(1024)
        file = open(mensaje, 'wb')
        file.write(cliente_message)
        file.close()

    else:
        flist=open("list.txt", 'r')
        comprueba=False
        fichero = flist.readline()
        while fichero != "": 
            if (mensaje+'\n')==fichero:
                comprueba = True
            fichero=flist.readline()
        flist.close()
        if comprueba==False:
            socket_cliente.send("error")
        else:
            file = open(mensaje, 'rb')
            data_file = file.read(1024)
            file.close()
            socket_cliente.send(data_file)


sock.close()
socket_cliente.close()



