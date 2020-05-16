import requests

page = "http://localhost:8081/send"
modify = "http://localhost:8081/modify"
consulta = "http://localhost:8081/listado"
consultaid = "http://localhost:8081/conshabit/"


while True:
	
	print("Elige la opcion que deseas realizar:")
	print("\t1. Dar de alta una nueva habitacion")
	print("\t2. Modificar los datos de una habitacion.")
	print("\t3. Consultar la lista completa de habitaciones.")
	print("\t4. Consultar una habitacion mediante identificador.")
	print("\t5. Consultar la lista de habitaciones ocupadas o desocupadas\n")

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



	elif (response == '3'):
		r = requests.get(url = consulta)
		message = r.json()
		print("\n\t~~~~~DATOS DE HABITACIONES~~~~~\n")
		print( "==========================================")
		for i in message['dict']:
			print ("Id. habitación: "+i['Identificador'])
			print ("Num. plazas disponibles: "+i['num_plazas'])
			print( "==========================================")

		print("\n")
		


	elif (response == '4'):
		resp = input("Introduce el identificador de la habitacion: ")
		consulta_aux = consultaid+resp;
		r = requests.get(url = consulta_aux)
		message = r.json()
		
		if (message['dict']['Identificador'] == 'no encontrado'):
			print( "==========================================")
			print("\n\t!IDENTIFICADOR NO ENCONTRADO!\n")
			print( "==========================================\n")
		else:
			print( "==========================================")
			print ("Id. habitación: "+message['dict']['Identificador'])
			print ("Num. plazas disponibles: "+message['dict']['num_plazas'])
			print( "==========================================\n")
			
		


	elif (response == '5'):
		print("Respuesta no valida")

	else:
		print("Respuesta no valida")
		r = requests.get(url = page)
		message = r.content
		print(message)



