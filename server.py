from bottle import Bottle, run, route, post, get, request
import os.path as path
import json
import os


#Comprobación del fichero data.json

if path.exists('data.json'):
	f = open('data.json', 'r+')
	contenido = f.read()
	if contenido=='':
		f.write("[]")
	f.close()
else:
	os.system("touch data.json")
	f = open('data.json', 'w')
	f.write("[]")
	f.close()


#Backup del archivo data.json

response = input("¿Desea hacer un backup?: (si/no) ")

if response == 'si':
	f = open('data.json', 'r')
	contenido = f.read()
	os.system("touch backup.json")
	g = open('backup.json', 'w')
	g.write(contenido)
	g.close()
	f.close()

no_encontrado = [{'Identificador': 'no encontrado'}]



#Definición de rutas

@post('/send')
def anadir():
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)

	lista_aux = {'Identificador': request.json.get('Identificador'), 'num_plazas':request.json.get('num_plazas'), 'equipamiento':request.json.get('equipamiento'), 'ocupada':request.json.get('ocupada')}
	
	encontrado = False

	d1 = json.dumps(habitacion) #Lo convierte a un diccionario de json
	d2 = json.loads(d1)
	for key in d2:
		if (key['Identificador'] == lista_aux['Identificador']):
			encontrado = True

	if(encontrado == False):
			habitacion.append(lista_aux)
			print("Añadido correctamente")

	else:
		print("Identificador repetido")
	
	with open('data.json', 'w') as fichero:
		json.dump(habitacion,fichero)	
		



@post('/modify/<id>')
def modificar(id):
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)

	lista_aux = {'Identificador': id, 'num_plazas':request.json.get('num_plazas'), 'equipamiento':request.json.get('equipamiento'), 'ocupada':request.json.get('ocupada')}
	print(lista_aux['Identificador'])
	encontrado = False

	for i in habitacion:
		if (i['Identificador'] == lista_aux['Identificador']):
			habitacion.remove(i)
			encontrado = True

	if(encontrado == True):
		habitacion.append(lista_aux)
		print("Actualizado correctamente")

	else:
		print("NO se ha encontrado la habitacion")

	with open('data.json', 'w') as fichero:
		json.dump(habitacion,fichero)



@get('/listado')
def mostrar_habitaciones():
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)
	return dict(dict = habitacion)



@get('/conshabit/<id>')
def consultar_habitacion(id):
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)
	
	encontrado = False
	for i in habitacion:
		if (i['Identificador'] == id):
			encontrado = True
			return dict (dict = i)

	if(encontrado == False):
		return dict (dict = {'Identificador': 'no encontrado'})



@get('/listaocup/<decision>')
def mostrar_ocupadas(decision):
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)
	lista = []

	encontrado = False
	for i in habitacion:
		if (i['ocupada'] == decision):
			encontrado = True
			lista.append(i)
	
	if(encontrado == False):
		return dict (dict = no_encontrado)

	else:
		return dict (dict = lista)


@get('/existe/<id>')
def existir(id):
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)

	encontrado = False
	for i in habitacion:
		if (i['Identificador'] == id):
			encontrado = True


	if(encontrado == False):
		return "NO encontrado"
	
	else:
		return "SI encontrado"


@get('/plazas/<num>/<num2>')
def plazas_habitacion(num,num2):
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)
	
	lista = []
	encontrado = False
	
	for i in habitacion:
		if (int(i['num_plazas']) >= int(num) and int(i['num_plazas']) <= int(num2)):
			encontrado = True
			lista.append(i)
		
	if(encontrado == False):
		return dict (dict = no_encontrado)

	else:
		return dict (dict = lista)


@post('/remove/<id>')
def modificar(id):
	
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)
	
	encontrado = False

	for i in habitacion:
		if (i['Identificador'] == id):
			habitacion.remove(i)
			encontrado = True

	if(encontrado == True):
		print("Borrado correctamente")

	else:
		print("NO se ha encontrado la habitacion")


	with open('data.json', 'w') as fichero:
		json.dump(habitacion,fichero)



run(host = 'localhost', port = 8081, debug = True)
