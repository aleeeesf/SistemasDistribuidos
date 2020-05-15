from bottle import Bottle, run, route, post, get
import json

@route('/')
def inicio():
    return '<h1>Pedro que funciona!!!!!!!!</h1>'

@get('/prueba')
def menu():
	return "funciona"

@get('/habitacion/<id>')
def devolver_identificador(id):

	file = open('data.json',)
	data = json.load(file)

	enviar = []
	for i in data['Habitacion']:
		if i['Identificador'] == id:
			print(i['Identificador'])
			return i['Identificador']

@get('/datoshabitacion/<id>')
def devolver_identificador(id):

	file = open('data.json',)
	data = json.load(file)

	enviar = []
	for i in data['Habitacion']:
		if i['Identificador'] == id:




#@post('/subir')
#def subida():

run(host = 'localhost', port = 8080, debug = True)