from mysql_conexion import *


def unidades_vendidas():
    """
    Se solicita a la base de datos un listado que contenga la cantidad
    de unidades vendidas por producto.

    """

    query = """select p.nombre_producto as Producto, sum(d.cantidad) as 'Unidades vendiadas' from detalle_venta d
               inner join producto p on p.id_productos = d.id_producto 
               group by p.nombre_producto
               order by sum(d.cantidad) desc;"""

    resultado = conexion(query, datos=None, tipo=1)

    return resultado


def productos_vendidos_x_mes():
    """
    Se solicita a la base de datos un listado con la cantidad de productos vendidos por mes.

    """

    query = """select monthname(v.fecha_venta) as MES , 
                p.nombre_producto as Producto , 
                sum(d.cantidad) as 'Unidades Vendidas',
                rank() over(partition by monthname(v.fecha_venta) order by sum(d.cantidad) desc) as Ranking  
                from detalle_venta d
                inner join producto p on p.id_producto = d.id_producto
                inner join venta v on v.id_venta = d.id_venta
                group by monthname(v.fecha_venta) , p.nombre_producto; """

    resultado = conexion(query, None, 1)

    return resultado


def ventas_por_empleado():
    """
    Se solicita a la base de datos un listado con la cantidad de

    """

    query = """select e.nombre_empleado AS 'Empleado', count(*) as 'Ventas' from empleado e
                inner join venta d on d.id_empleado = e.id_empleado
                group by e.nombre_empleado
                order by count(*) desc;"""
    resultado = conexion(query, None, 1)

    return resultado


def ventas_x_mes():
    """
    Se solicita un listado con la cantidad de ventas por mes.

    """

    query = """select monthname(fecha_venta) as MES, count(*) as Cantidad from venta
                group by monthname(fecha_venta);"""

    resultado = conexion(query, None, 1)

    return resultado


def CRUD():
    """
    Se realiza un CRUD de la tabla productos.

    """
    while True:

        print('=' * 5)
        print('1. Mostrar productos.')
        print('2. Insertar producto BonOBon.')
        print('3. Actualizar producto BonOBon.')
        print('4. Eliminar producto BonOBon.')
        print('5. Salir.')
        print('=' * 5)
        opcion = input('Ingrese una opcion: ')


        if opcion == '1':
            query = """SELECT nombre_producto FROM producto;"""
            resultado = conexion(query, None, 1)

            return resultado

        elif opcion == '2':
            query = """INSERT INTO producto(nombre_producto, tipo_producto, unidades, precio_venta, vencimiento, id_proveedor)
                        VALUES (%s, %s, %s, %s, %s, %s);"""
            datos =  ('BonOBon', 1, 1000, 500, "2026-09-19 10:15:14", 2)

            id = conexion(query, datos, 2)

            print(f'El producto Bon O Bon con id: {id}')

        elif opcion == '3':
            query = """UPDATE producto SET precio_venta = %s where nombre_producto = %s;"""

            datos = (750, 'BonOBon')

            id = conexion(query, datos, 2)

            print(f'El producto con ID: {id} a sido actualizado con exito.')

        elif opcion == '4':
            query = """DELETE FROM producto WHERE nombre_producto = %s;"""

            datos = ('BonOBon',)

            conexion(query, datos, 4)

            print('El Producto BonOBon a sido eliminado con exito.')

        elif opcion == '5':
            pass
        else:
            print('Opcion incorrecta')


if __name__ == '__main__':
    CRUD()
