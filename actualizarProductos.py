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
		conexion = sqlite3.connect("INVENTARIO.db")
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
				nuevoPrecio = input('Precio unitario (dejar en blanco de ser necesario): ')
				if nuevoPrecio == '':		#en blanco inserta valor NULL en la tabla
					break
				else:
					try:
						float(nuevoPrecio)
						break
					except ValueError:
						print('El precio ingresado no es válido. Intente nuevamente: ')
						continue
			
			query = f"""UPDATE PRODUCTOS SET 'PRECIO' = {nuevoPrecio} WHERE 'ID' = {idProducto}"""
			
			cursor.execute(query)
			conexion.close()
			
		elif opcion == 5:
		
			while True:
				nuevaUbicacion = input('Nº de estante de depósito (dejar en blanco de ser necesario): ')
				if nuevaUbicacion == '':			
					break
				else:
					try:
						int(nuevaUbicacion)
						break
					except ValueError:
						print('La ubicación ingresada no es válida. Intente nuevamente: ')
						continue
					
			query = f"""UPDATE PRODUCTOS SET 'UBICACION' = {nuevaUbicacion} WHERE 'ID' = {idProducto}"""
			
			cursor.execute(query)
			conexion.close()
			
		elif opcion == 6:
		
			while True:
				nuevoProveedor = input('Proveedor registrado (dejar en blanco de ser necesario): ')
				if nuevoProveedor == '':
					break
				else:
					try:
						str(nuevoProveedor)
						break
					except ValueError:
						print('El proveedor ingresado no es válido. Intente nuevamente: ')
						continue
				
			query = f"""UPDATE PRODUCTOS SET 'PROVEEDOR' = {nuevoProveedor} WHERE 'ID' = {idProducto}"""
			
			cursor.execute(query)
			conexion.close()
			
		elif opcion == 7:
		
			conexion.close()
			break
