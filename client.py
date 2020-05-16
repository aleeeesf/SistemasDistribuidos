import requests

page = "http://localhost:8081/send"
modify = "http://localhost:8081/modify"


print("Elige la opcion que deseas realizar:")
print("1. Dar de alta una nueva habitacion")
print("2. Modificar los datos de una habitacion.")
print("3. Consultar la lista completa de habitaciones.")
print("4. Consultar una habitacion mediante identificador.")
print("5. Consultar la lista de habitaciones ocupadas o desocupadas")

while True:
	
	response = input("Introduce respuesta: ")
	
	if (response == '1'):
		num_hab = input("Introduce identificador de la habitacion: ")
		plazas = input("\nIntroduce plazas de la habitacion: ")
		lista = {'Identificador' : num_hab,'num_plazas' : plazas}
		requests.post(page, json = lista)
		print(lista)

	elif (response == '2'):
		num_hab = input("Introduce identificador de la habitacion: ")
		plazas = input("Introduce plazas de la habitacion: ")
		lista = {'Identificador' : num_hab,'num_plazas' : plazas}
		requests.post(modify, json = lista)
		print(lista)



	elif (response == 3):
		print("Respuesta no valida")


	elif (response == 4):
		resp = input("Introduce el identificador de la habitacion:")



	elif (response == 5):
		print("Respuesta no valida")

	else:
		print("Respuesta no valida")
		r = requests.get(url = page)
		message = r.content
		print(message)



