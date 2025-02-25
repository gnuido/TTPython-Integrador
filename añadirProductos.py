#añadirProductos.py

def menuSecundario():
	
	subMenu = [	'1> Añadir un nuevo producto.',
				'2> Volver al menú anterior.'	]
	
	opcion = ''
	while opcion != 2:
		print('Seleccione una de las siguientes opciones: ')
		for i in subMenu:
			print(i)
		
		import controlOpciones
		opcion = controlOpciones.verificador(subMenu)
		
#--------------
		import sqlite3
		conexion = sqlite3.connect("INVENTARIO.db")
		cursor = conexion.cursor()
		
		if opcion == 1:
			
			while True:
				try:
					marca = str(input('Marca comercial: '))
					break
				except ValueError:
					print('La marca comercial ingresada posee un formato no válido. Intente nuevamente: ')
					continue
		
			while True:
				try:
					descripcion = str(input('Descripción del producto: '))
					break
				except ValueError:
					print('La descripción ingresada posee un formato no válido. Intente nuevamente: ')
					continue
				
			while True:
				try:
					cantidad = int(input('Cantidad en stock: '))
					break
				except ValueError:
					print('La cantidad ingresada no es válida. Intente nuevamente: ')
					continue		
		
			while True:
				try:
					precio = float(input('Precio unitario (dejar en blanco de ser necesario): '))
					break
				except ValueError:
					print('El precio ingresado no es válido. Intente nuevamente: ')
					continue
				
			while True:
				try:
					ubicacion = int(input('Nº de estante de depósito (dejar en blanco de ser necesario): '))
					break
				except ValueError:
					print('El número ingresado no es válido. Intente nuevamente: ')
					continue
		
			while True:
				try:
					proveedor = str(input('Proveedor registrado (dejar en blanco de ser necesario): '))
					break
				except ValueError:
					print('El nombre ingresado no es válido. Intente nuevamente: ')
					continue

			query = """INSERT INTO PRODUCTOS ('MARCA', 'DESCRIPCION', 'CANTIDAD', 'PRECIO', 'UBICACION', 'PROVEEDOR')
					VALUES (?, ?, ?, ?, ?, ?)"""
			
			cursor.execute(query, (marca, descripcion, cantidad, precio, ubicacion, proveedor))	
		
			print('Se ha añadido el producto de forma exitosa')
		
			conexion.close()
			continue
	
#%%%%%%			
		elif opcion == 2:
			
			conexion.close()
			continue
			
				
		
