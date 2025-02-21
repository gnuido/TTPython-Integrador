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
