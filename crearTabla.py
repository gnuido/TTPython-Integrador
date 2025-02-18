#crearTabla.py

import sqlite3
#implementar doble comillas y mayúsculas en lo posible para código de sqlite3

def crear():
	conexion = sqlite3.connect("INVENTARIO.DB")
	cursor = conexion.cursor()

	cursor.execute(	"""CREATE TABLE IF NOT EXISTS "PRODUCTOS" (
					"ID",
					"MARCA" TEXT NOT NULL,
					"DESCRIPCION" TEXT NOT NULL,
					"CANTIDAD" INTEGER NOT NULL,
					"PRECIO" REAL,
					"UBICACION" INTEGER,
					"PROVEEDORES" TEXT,
					PRIMARY KEY("ID"))"""	)
					
	print('Tabla "PRODUCTOS" creada exitosamente.')
	
	conexion.close()
