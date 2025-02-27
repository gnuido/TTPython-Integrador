#buscarProductos.py

def menuSecundario():
	
	subMenu = [	'1> Buscar productos por ID.',
				'2> Buscar productos por marca comercial.',
				'3> Buscar productos por ubicación.',
				'4> Buscar productos por proveedor.',
				'5> Volver al menú anterior.'				]
	
	opcion = ''
	while opcion != 5:
		print('Seleccione una de las siguientes opciones: ')
		for i in subMenu:
			print(i)
			
		import controlOpciones
		opcion = controlOpciones.verificador(subMenu)
	
#--------------
		import sqlite3
		conexion = sqlite3.connect("INVENTARIO.db")
		cursor = conexion.cursor()
	
#%%%%%%
		if opcion == 1:
		
			while True:		#verificar validez del ID
				try:
					ID = int(input('Ingrese el ID del producto: '))
					break
				except ValueError:
					print('El número de ID ingresado no es válido. Intente nuevamente: ')
					continue

			query = f"""SELECT * FROM PRODUCTOS WHERE 'ID' = {ID}"""
		
			cursor.execute(query)
			lista = cursor.fetchall()		#ID único, debiese devolver un solo resultado
		
			conexion.close()
		
			if len(lista) == 0:
				print('No se hallaron productos que coincidan con el ID ingresado')
			else:
				print(lista)
			
#%%%%%%
		elif opcion == 2:
		
			while True:
				try:
					marca = str(input('Ingrese la marca comercial del producto: '))
					break
				except ValueError:
					print('La marca ingresada posee un formato no válido. Intente nuevamente: ')
					continue
					
			query = f"""SELECT * FROM PRODUCTOS WHERE 'MARCA' = {marca}"""
		
			while True:			#gestión búsquedas exitosas o fallidas	
				try:
					cursor.execute(query)
					lista = cursor.fetchall()
					break
				except sqlite3.OperationalError:
					lista = []		#se crea la lista vacía si el input no coincide con ningún campo de la tabla
					break
					
			conexion.close()
		
			if len(lista) == 0:
				print('No hay productos que coincidan con la marca ingresada.')
			else:
				print(lista)
			
#%%%%%%
		elif opcion == 3:
		
			while True:
				try:
					ubicacion = int(input('Ingrese el número de estante: '))
					break
				except ValueError:
					print('El número de estante ingresado no es válido. Intente nuevamente: ')
					continue
		
			query = f"""SELECT * FROM PRODUCTOS WHERE 'UBICACION' = {ubicacion}"""
	
			cursor.execute(query)
			lista = cursor.fetchall()
	
			conexion.close()
	
			if len(lista) == 0:
				print('No hay productos que coincidan con el estante ingresado.')
			else:
				print(lista)
		
#%%%%%%
		elif opcion == 4:
		
			while True:
				try:
					proveedor = str(input('Ingrese el nombre del proveedor: '))
					break
				except ValueError:
					print('El proveedor ingresado posee un formato no válido. Intente nuevamente: ')
					continue
		
			query = f"""SELECT * FROM PRODUCTOS WHERE 'PROVEEDOR' = {proveedor}"""
	
			while True:
				try:
					cursor.execute(query)
					lista = cursor.fetchall()
					break
				except sqlite3.OperationalError:
					lista = []
					break
					
			conexion.close()
	
			if len(lista) == 0:
				print('No hay productos que coincidan con el proveedor ingresado.')
			else:
				print(lista)
		
#%%%%%%
		elif opcion == 5:
		
			conexion.close()
			continue				#volver al menú anterior (principal)
