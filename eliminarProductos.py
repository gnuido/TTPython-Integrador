#eliminarProductos.py

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

		subMenu = [	'1> Eliminar un producto.',
					'2> Volver al menú anterior.'	]
					
		import controlOpciones
		opcion = controlOpciones.verificador(subMenu)

	#--------------	
		import sqlite3
		conexion = sqlite3.connect("INVENTARIO.db")
		cursor = conexion.cursor()
		
		if opcion == 1:
		
			query = f"""DELETE FROM PRODUCTOS WHERE 'ID' = {idProducto}"""
		
			cursor.execute(query)
			conexion.close()
			continue
			
		elif opcion == 2:
			
			conexion.close()
			break
