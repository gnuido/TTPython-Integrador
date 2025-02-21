#actualizarProductos.py

def menuSecundario():
	
	while True:
		try:
			idProducto = int(input('Ingrese el ID del producto a modificar (ingrese 0 para volver al menú anterior): '))
			if idProducto != 0:
				opcion = ''	
			else:
				opcion = 7		#escape en caso de necesitar volver al menú principal para buscar la ID del producto
				
		except ValueError:
			print('El ID ingresado no es válido. Intente nuevamente: ')
			continue

	subMenu = [	'1> Actualizar marca.',
				'2> Actualizar descripción.',
				'3> Actualizar cantidad.',
				'4> Actualizar precio.',
				'5> Actualizar ubicación.',
				'6> Actualizar proveedor.',
				'7> Volver al menú anterior.'	]
				
	while opcion != 7:
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
			
			while True:
				try:
					nuevaMarca = str(input('Marca comercial: '))
					break
				except ValueError:
					print('La marca comercial ingresada no es válida. Intente nuevamente: ')
					continue
					
			query = f"""UPDATE PRODUCTOS SET 'MARCA' = {nuevaMarca} WHERE 'ID' = {idProducto}"""
			
			cursor.execute(query)
			conexion.close()
			
		elif opcion == 2:
			
			while True:
				try:
					nuevaDescripcion = str(input('Descripción del producto: '))
					break
				except ValueError:
					print('La descripción ingresada posee un formato no válido. Intente nuevamente: ')
					continue
					
			query = f"""UPDATE PRODUCTOS SET 'DESCRIPCION' = {nuevaDescripcion} WHERE 'ID' = {idProducto}"""
			
			cursor.execute(query)
			conexion.close()
			
		elif opcion == 3:
			
			while True:
				try:
					nuevaCantidad = int(input('Cantidad en stock: '))
					break
				except ValueError:
					print('La cantidad ingresada no es válida. Intente nuevamente: ')
					continue
					
			query = f"""UPDATE PRODUCTOS SET 'CANTIDAD' = {nuevaCantidad} WHERE 'ID' = {idProductos}"""
			
			cursor.execute(query)
			conexion.close()
			
		elif opcion == 4:
			
			while True:
				nuevoPrecio = float(input('Precio unitario (dejar en blanco de ser necesario): '))
				break
			except ValueError:
				print('El precio ingresado no es válido. Intente nuevamente: ')
				continue
				
			query = f"""UPDATE PRODUCTOS SET 'PRECIO' = {nuevoPrecio} WHERE 'ID' = {idProducto}"""
			
			cursor.execute(query)
			conexion.close()
			
		elif opcion == 5:
			
			while True:
				nuevaUbicacíon = int(input('Nº de estante de depósito (dejar en blanco de ser necesario): '))
