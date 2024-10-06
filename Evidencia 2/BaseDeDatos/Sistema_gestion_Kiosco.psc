Algoritmo Sistema_gestion_Kiosco
	Definir id_empleados, id_productos, id_sucursal, unidades, id_ventas, cantidad, DNI_empleado, menu Como Entero
	Definir nombre_proveedor, apellido_proveedor, email_proveedor, direccion, nombre_producto, tipo_producto, direccion_sucursal, nombre_sucursal, email_sucursal, encargado, nombre_empleado, apellido_empleado, cargo, mododepago Como Cadena
	Definir precio_venta, total, salario Como Real
	Escribir 'Seleccione una opcion'
	Escribir '1- Empleados'
	Escribir '2- Proveedores'
	Escribir '3- Productos'
	Escribir '4- Sucursal'
	Leer menu
	
	Según menu Hacer
		1:
			Escribir '1- Alta de empleado'
			Escribir '2- Baja de empleado'
			Escribir '3- Editar informacion de empleado'
		2:
			Escribir '1- Nuevo proveedor'
			Escribir '2- Borrar proveedor'
			Escribir '3- Editar informacion de proveedor'
		3:
			Escribir '1- Ver informacion de producto'
			Escribir '2- Sumar producto nuevo'
			Escribir '3- Borrar producto'
			Escribir '4- Editar informacion de un producto'
		4:
			Escribir '1- Ver sucursal'
			Escribir '2- Agregar una nueva sucursal'
			Escribir '3- Borrar sucursal'
			Escribir '4- Editar informacion de sucursal'
		De Otro Modo:
			Escribir 'Opcion incorrecta, seleccione otra opcion'
	FinSegún
FinAlgoritmo
