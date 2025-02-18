#main.py

import crearTabla
crearTabla.crear()

menuPrincipal = [	'1> Mostrar lista de productos.',
					'2> Buscar producto de la lista.',
					'3> Añadir productos a la lista.',
					'4> Actualizar producto de la lista.',
					'5> Eliminar producto de la lista.',
					'6> Ayuda/FAQ',
					'7> Salir.'								]
					
for i in menuPrincipal:
	print(i)

#menú principal
import controlOpciones
opcion = controlOpciones.verificador(menuPrincipal)

