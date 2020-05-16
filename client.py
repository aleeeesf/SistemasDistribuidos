import requests

page = "http://localhost:8081/send"
modify = "http://localhost:8081/modify/"
consulta = "http://localhost:8081/listado"
consultaid = "http://localhost:8081/conshabit/"
habocupadas = "http://localhost:8081/listaocup/"
exists = "http://localhost:8081/existe/"
plaza = "http://localhost:8081/plazas/"
remover = "http://localhost:8081/remove/"

check = True
while check:
	
	print("Elige la opcion que deseas realizar:")
	print("\t1. Dar de alta una nueva habitacion")
	print("\t2. Modificar los datos de una habitacion.")
	print("\t3. Consultar la lista completa de habitaciones.")
	print("\t4. Consultar una habitacion mediante identificador.")
	print("\t5. Consultar la lista de habitaciones ocupadas o desocupadas")
	print("\t6. Consultar el numero de habitaciones con las plazas deseadas")
	print("\t7. Borrar una habitacion")
	print("\t8. Salir\n")



	response = input("Introduce respuesta: ")
	
	if (response == '1'):
		num_hab = input("Introduce identificador de la habitacion: ")
		req = requests.get(url = exists+num_hab)
		data = req.text

		if(data == "SI encontrado"):
			print("\n*****************************************")
			print("\n\tLA HABITACION YA EXISTE\n")
			print("*****************************************\n")

		else:
			
			plazas = input("Introduce plazas de la habitacion: ")
			equip = input("Introduce lista de equipamientos: ")
			ocup = input("¿Ocupada? (si/no): ")

			if(ocup != "si" and ocup != "no"):
				print("\n***Error, respuesta distinta a si o no***")

			else:
				lista = {'Identificador' : num_hab,'num_plazas' : plazas, 'equipamiento': equip, 'ocupada': ocup}
				requests.post(page, json = lista)
				
				print("\n*****************************************")
				print("\n\tAÑADIDA CORRECTAMENTE\n")
				print("*****************************************\n")

	elif (response == '2'):
		
		num_hab = input("Introduce identificador de la habitacion: ")
		req = requests.get(url = exists+num_hab)
		data = req.text

		if(data == "NO encontrado"):
			print("\n************************************************")
			print("\n\tNO SE HA ENCONTRADO LA HABITACION\n")
			print("************************************************\n")
		
		else:
			plazas = input("Introduce plazas de la habitacion: ")
			equip = input("Introduce lista de equipamientos: ")
			ocup = input("¿Ocupada? (si/no): ")
			lista = {'num_plazas' : plazas, 'equipamiento': equip, 'ocupada': ocup}
			requests.post(modify+num_hab, json = lista)
			
			print("\n**********************************************")
			print("\n\tSE HA ACTUALIZADO CORRECTAMENTE\n")
			print("**********************************************\n")


	elif (response == '3'):
		r = requests.get(url = consulta)
		message = r.json()
		
		print("\n\t~~~~~DATOS DE HABITACIONES~~~~~\n")
		
		
		for i in message['dict']:
			print("==========================================")
			print ("Id. habitación: "+i['Identificador'])
			print ("Num. plazas disponibles: "+i['num_plazas'])
			print ("Lista de equipamientos: "+i['equipamiento'])
			print ("Ocupada: "+i['ocupada'])
			print ("==========================================\n")

		

	elif (response == '4'):
		resp = input("Introduce el identificador de la habitacion: ")
		consulta_aux = consultaid+resp;
		r = requests.get(url = consulta_aux)
		message = r.json()
		
		if (message['dict']['Identificador'] == 'no encontrado'):
			print ("\n==========================================")
			print ("\n\t!IDENTIFICADOR NO ENCONTRADO!\n")
			print ("==========================================\n")
		
		else:
			print( "\n==========================================")
			print ("Id. habitación: "+message['dict']['Identificador'])
			print ("Num. plazas disponibles: "+message['dict']['num_plazas'])
			print ("Lista de equipamientos: "+message['dict']['equipamiento'])
			print ("Ocupada: "+message['dict']['ocupada'])
			print ("==========================================\n")
			
		


	elif (response == '5'):
		
		print("¿Que desea: ?")
		resp = input("1. Ocupadas (Respoder si)\n2. No ocupadas (Respoder no)\n")

		if(resp != 'si' and resp != 'no'):
			print("\n***Error, respuesta diferente a si o no***")
		else:
			r = requests.get(url = habocupadas+resp)
			message = r.json()
			
			for i in message['dict']:
				if (i['Identificador'] == 'no encontrado'):
					print ("\n==========================================")
					print ("\n\t¡ NO SE HAN ENCONTRADO HABITACIONES !\n")
					print ("==========================================\n")
				else:
					print( "\n==========================================")
					print ("Id. habitación: "+i['Identificador'])
					print ("Num. plazas disponibles: "+i['num_plazas'])
					print ("Lista de equipamientos: "+i['equipamiento'])
					print ("Ocupada: "+i['ocupada'])
					print ("==========================================\n")

	
	elif (response == '6'):
		
		print("Introduzca el intervalo de plazas")
		resp1 = input("Limite inferior de plazas: ")
		resp2 = input("Limite superior de plazas: ")

		if(int(resp1) > int(resp2)):
			print("Error, intervalo mal introducido")
		else:
			r = requests.get(url = plaza+resp1+"/"+resp2)
			message = r.json()
			
			print("\n")
			for i in message['dict']:
				if (i['Identificador'] == 'no encontrado'):
					print ("\n==========================================")
					print ("\n\t¡ NO SE HAN ENCONTRADO HABITACIONES !\n")
					print ("==========================================\n")
				else:
					print( "==========================================")
					print ("Id. habitación: "+i['Identificador'])
					print ("Num. plazas disponibles: "+i['num_plazas'])
					print ("Lista de equipamientos: "+i['equipamiento'])
					print ("Ocupada: "+i['ocupada'])
					print ("==========================================\n")


	elif (response == '7'):
		num_hab = input("Introduce identificador de la habitacion: ")
		req = requests.get(url = exists+num_hab)
		data = req.text

		if(data == "NO encontrado"):
			print("\n************************************************")
			print("\n\tNO SE HA ENCONTRADO LA HABITACION\n")
			print("************************************************\n")
		else:
			requests.post(remover+num_hab)
			print("\n**********************************************")
			print("\n\tSE HA BORRADO CORRECTAMENTE\n")
			print("**********************************************\n")

	

	elif (response == '8'):
		check = False


	else:
		print("Respuesta no valida")
		r = requests.get(url = page)
		message = r.content
		print(message)



