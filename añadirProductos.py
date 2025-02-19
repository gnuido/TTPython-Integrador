#añadirProductos.py

def menuSecundario():
	
	subMenu = [	'1> Añadir un nuevo producto.',
				'2> Volver al menú anterior.'	]
	
	opcion = ''
	while opcion != 2:
		print('Seleccione una de las siguientes opciones: ')
		for i in subMenu():
			print(i)
		
		import controlOpciones
		opcion = controlOpciones.verificador(subMenu)
		
#--------------
