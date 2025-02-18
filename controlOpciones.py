#controlOpciones.py

def verificador(menuActual):	#menú actual es el menú desde el cual se llama a la función

	while True:				#verificador de valor numérico
	
		try:
			opcion = int(input(''))
			
			if (0 < opcion <= len(menuActual)) == False:					#verificador de opción disponible en menú
				print('La opción ingresada no se encuentra en el menú. Intente nuevamente: ')
				continue
			else:
				return(opcion)
			
			break
			
		except ValueError:
			print('La opción seleccionada no es válida. Intente nuevamente: ')
			continue
