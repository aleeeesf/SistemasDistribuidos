from bottle import Bottle, run, route, post, get, request
import json


habitacion = [{'Identificador' : '14145', 'num_plazas' : '12', 'equipamiento': 'televisor, wi-fi', 'ocupada':'si'},{'Identificador' : '1613', 'num_plazas' : '14', 'equipamiento': 'cama', 'ocupada':'si'},{'Identificador' : '120', 'num_plazas' : '3', 'equipamiento':'cortinas', 'ocupada':'no'}]

#@get('/habitacion/<id>')
#def devolver_identificador(id):

	#file = open('prebajson.json',)
	#data = json.load(file)

@post('/send')
def anadir():
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
		
		



@post('/modify/<id>')
def modificar(id):
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



@get('/listado')
def mostrar_habitaciones():
	return dict(dict = habitacion)



@get('/conshabit/<id>')
def consultar_habitacion(id):

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


run(host = 'localhost', port = 8081, debug = True)
