#mostrarProductos.py

def menuSecundario():
	
	subMenu = [	'1> Ver lista de productos completa.',
				'2> Ver lista de productos fuera de stock.',
				'3> Ver lista de productos sin ubicar.',
				'4> Ver lista de productos sin proveedores.',
				'5> Volver al menú anterior.']
	
	opcion = ''
	while opcion != 5:
		print('Seleccione una de las siguientes opciones: ')
		for i in subMenu:
			print(i)
	
		import controlOpciones
		opcion = controlOpciones.verificador(subMenu)
	
#--------------
		import sqlite3
		conexion = sqlite3.connect("INVENTARIO.DB")
		cursor = conexion.cursor()
		
		if opcion == 1:
			query = """SELECT * FROM PRODUCTOS"""
			
		elif opcion == 2:
			query = """SELECT * FROM PRODUCTOS WHERE "CANTIDAD" = 0"""
			
		elif opcion == 3:
			query = """SELECT * FROM PRODUCTOS WHERE "UBICACION" = NULL"""
		
		elif opcion == 4:
			query = """SELECT * FROM PRODUCTOS WHERE "PROVEEDORES" = NULL"""
			
		elif opcion == 5:
			conexion.close()
			break
			
		cursor.execute(query)
		lista = cursor.fetchall()
		
		conexion.close()

		if len(lista) == 0:
			print('No hay productos para mostrar.') 
		else:
			for	i in lista:
				print(i)
			
