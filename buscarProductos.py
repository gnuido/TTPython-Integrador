#buscarProductos.py

def menuSecundario():
	
	subMenu = [	'1> Buscar productos por ID.',
				'2> Buscar productos por marca comercial.',
				'3> Buscar productos por ubicación.',
				'4>	Buscar productos por proveedor.',
				'5> Volver al menú anterior.'				]
	
	opcion = ''
	while opcion != 5:
		print('Seleccione una de las siguientes opciones: ')
		for i in subMenu:
			print(i)
			
		import controlOpciones
		opcion = controlOpciones.verficador(subMenu)
	
#--------------
	import sqlite3
	conexion = sqlite3.connect("INVENTARIO.DB")
	cursor = conexion.cursor()
	
	if opcion == 1:
		
