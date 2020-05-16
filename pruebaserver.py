from bottle import Bottle, run, route, post, get, request
import json
#@get('/habitacion/<id>')
#def devolver_identificador(id):

	#file = open('prebajson.json',)
	#data = json.load(file)

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
			print(habitacion)
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

	#d1 = json.dumps(habitacion) #Lo convierte a un diccionario de json
	#d2 = json.loads(d1)
	for i in habitacion:
		if (i['Identificador'] == lista_aux['Identificador']):
			habitacion.remove(i)
			encontrado = True

	if(encontrado == True):
		habitacion.append(lista_aux)
		print("Actualizado correctamente")

	else:
		print("NO se ha encontrado la habitacion")

	for i in habitacion:
		print (i)

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
			print(i)
			encontrado = True
			return dict (dict = i)

	if(encontrado == False):
		return dict (dict = {'Identificador': 'no encontrado'})



@get('/listaocup/<decision>')
def mostrar_ocupadas(decision):
	with open('data.json', 'r') as fichero:
		habitacion = json.load(fichero)
	lista = []
	print(decision)
	encontrado = False
	for i in habitacion:
		if (i['ocupada'] == decision):
			encontrado = True
			lista.append(i)
		

	print(lista)
	if(encontrado == False):
		return dict (dict = [{'Identificador': 'no encontrado'}])

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
		

	print(lista)
	if(encontrado == False):
		return dict (dict = [{'Identificador': 'no encontrado'}])

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

	for i in habitacion:
		print (i)

	with open('data.json', 'w') as fichero:
		json.dump(habitacion,fichero)

run(host = 'localhost', port = 8081, debug = True)
