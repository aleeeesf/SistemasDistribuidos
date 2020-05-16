from bottle import Bottle, run, route, post, get, request
import json


habitacion = [{'Identificador' : '14145', 'num_plazas' : '12'},{'Identificador' : '1613', 'num_plazas' : '14'},{'Identificador' : '120', 'num_plazas' : '3'}]

#@get('/habitacion/<id>')
#def devolver_identificador(id):

	#file = open('prebajson.json',)
	#data = json.load(file)

@post('/send')
def anadir():
	lista_aux = {'Identificador': request.json.get('Identificador'), 'num_plazas':request.json.get('num_plazas')}
	
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
		



@post('/modify')
def modificar():
	lista_aux = {'Identificador': request.json.get('Identificador'), 'num_plazas':request.json.get('num_plazas')}
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



run(host = 'localhost', port = 8081, debug = True)
