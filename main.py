#main.py

import crearTabla
crearTabla.crear()

#--------------
opcion = ''

menuPrincipal = [	'1> Mostrar lista de productos.',
					'2> Buscar producto de la lista.',
					'3> Añadir productos a la lista.',
					'4> Actualizar producto de la lista.',
					'5> Eliminar producto de la lista.',
					'6> Ayuda/FAQ',
					'7> Salir.'								]
					
while opcion != 7:
					
	for i in menuPrincipal:
		print(i)

	#menú principal
	import controlOpciones
	opcion = controlOpciones.verificador(menuPrincipal)
	
#--------------
	if opcion == 1:
		import mostrarProductos
		mostrarProductos.menuSecundario()
		continue
	
	elif opcion == 2:
		import buscarProductos
		buscarProductos.menuSecundario()
		continue
	
	elif opcion == 3:
		import añadirProductos
		añadirProductos.menuSecundario()
		continue
		
	elif opcion == 4:
			
