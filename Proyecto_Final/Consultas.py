import mysql.connector
from mysql.connector import errorcode
from mysql_conexion import *
from Formateador import *
import datetime


class Producto:
    def __init__(self, id=None, nombre=None, tipo=None, unidades=None, precio=None, vencimiento=None, id_proveedor=None):
        self._id = id
        self._nombre = nombre
        self._tipo = tipo
        self._unidades = unidades
        self._precio = precio
        self._vencimiento = vencimiento
        self._id_proveedor = id_proveedor

    def __str__(self):
        return f'|Id: {self._id}|Nombre: {self._nombre}|Tipo: {self._tipo}|Unidades: {self._unidades}|Precio: {self._precio}|Vencimiento: {self._vencimiento}|Proveedor: {self._id_proveedor}'


    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, value: str):
        if value.isdigit():
            raise Exception('El campo nombre no debe ser un numero.')
        self.nombre = value

    @property
    def tipo(self):
        return self.tipo

    @tipo.setter
    def tipo(self, value: str):
        if not value.isdigit():
            raise Exception('El campo tipo debe ser un numero.')
        if int(value) not in (1, 2, 3, 4, 5):
            raise Exception('Los valores permitidos para tipo son 1, 2, 3, 4, 5.')
        self.tipo = int(value)

    @property
    def unidades(self):
        return self.unidades

    @unidades.setter
    def unidades(self, value: str):
        if not value.isdigit():
            raise Exception('Las unidades deben ser un digito.')
        if not int(value) >= 0:
            raise Exception('Las unidades deben ser mayor a cero.')
        self.unidades = int(value)

    @property
    def precio(self):
        return self.precio

    @precio.setter
    def precio(self, value: str):
        try:
            precio = float(value)
        except ValueError:
            raise Exception('El campo precio debe ser un numero')
        if precio <= 0:
            raise Exception('El campo precio debe ser mayor a cero.')
        self.precio = precio

    @property
    def vencimiento(self):
        return self.vencimiento

    @vencimiento.setter
    def vencimiento(self, value: str):
        try:
            fecha = datetime.datetime.strptime(value, '%Y %M %d')
        except ValueError:
            raise Exception('El campo fecha debe seguir el siguiente formato YY/MM/DD')
        if fecha <= datetime.datetime.now():
            raise Exception(f'El campo fecha debe ser mayor a {datetime.datetime.now()}')
        self.vencimiento = fecha

    @property
    def id_proveedor(self):
        return self.id_proveedor

    @id_proveedor.setter
    def id_proveedor(self, value: str):
        if not value.isdigit():
            raise Exception('Las proveedor debe ser un digito.')
        if not int(value) >= 0:
            raise Exception('Las proveedor debe ser mayor a cero.')

        self.id_proveedor = int(value)

        query = """INSERT INTO producto(nombre_producto, tipo_producto, unidades, precio_venta, vencimiento, id_proveedor)
                               VALUES (%s, %s, %s, %s, %s, %s);"""
        datos = (self.nombre, self.tipo, self.unidades, self.precio, self.vencimiento, self.id_proveedor)

        id = conexion(query, datos, 2)

        print(f'Se registro el producto con id: {id}')


def unidades_vendidas():
    """
    Se solicita a la base de datos un listado que contenga la cantidad
    de unidades vendidas por producto.

    """

    query = """select p.nombre_producto as Producto, sum(d.cantidad) as 'Unidades vendiadas' from detalle_venta d
               inner join producto p on p.id_producto = d.id_producto 
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
    ventas por empleado.

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


def consultas():
    """

    """
    while True:

        print('=' * 5)
        print('1. Mostrar productos.')
        print('2. Insertar producto.')
        print('3. Actualizar producto.')
        print('4. Eliminar producto.')
        print('5. Unidades vendidas por producto.')
        print('6. Productos vendidos por mes.')
        print('7. Ventas por empleado.')
        print('8. Ventas por mes.')
        print('9. Salir.')
        print('=' * 5)
        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            try:
                query = """SELECT nombre_producto FROM producto;"""
                resultado = conexion(query, None, 1)

                formateador(resultado)
                print('\n' * 20)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue
                print(err)
        elif opcion == '2':
            try:
                nombre = input('Ingrese el nombre del producto: ')
                tipo = input('Ingrese el tipo del producto(1, 2, 3, 4, 5): ')
                unidades = input('Ingrese el numero de unidades: ')
                precio = input('Ingrese el precio de venta: ')
                vencimiento = input('Ingrese la fecha de vencimiento(YY/MM/DD): ')
                id_proveedor = input('Ingrese el id del proveedor: ')

                query = """INSERT INTO producto(nombre_producto, tipo_producto, unidades, precio_venta, vencimiento, id_proveedor)
                                               VALUES (%s, %s, %s, %s, %s, %s);"""
                datos = (nombre, tipo, unidades, precio, vencimiento, id_proveedor)

                id = conexion(query, datos, 2)

                print(f'Se registro el producto con id: {id}')

                continuar = input('Presione enter para continuar.....')

                print('\n' * 20)
            except mysql.connector.Error as err:
                if err.errno == errorcode.WARN_DATA_TRUNCATED:
                    print('\n' * 20)
                    print('Datos incorrectos(Revise el tipo y largo).')
                    continue
                if err.errno == errorcode.ER_TRUNCATED_WRONG_VALUE:
                    print('\n' * 20)
                    print('Datos incorrectos(Revise el tipo y largo).')
                    continue
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue

                print(err)
                print('\n' * 20)
                continue

        elif opcion == '3':

            try:
                nombre = input('Ingrese el nombre del producto: ')
                precio = input('Ingrese el precio de venta: ')
                query = """UPDATE producto SET precio_venta = %s where nombre_producto = %s;"""

                datos = (precio, nombre)

                id = conexion(query, datos, 2)
                print('\n' * 20)
                print(f'El producto a sido actualizado con exito.')

            except mysql.connector.Error as err:
                if err.errno == errorcode.WARN_DATA_TRUNCATED:
                    print('\n' * 20)
                    print('Datos incorrectos(Revise el tipo y largo).')
                    continue
                if err.errno == errorcode.ER_TRUNCATED_WRONG_VALUE:
                    print('\n' * 20)
                    print('Datos incorrectos(Revise el tipo y largo).')
                    continue
                if err.errno == errorcode.ER_TRUNCATED_WRONG_VALUE_FOR_FIELD:
                    print('\n' * 20)
                    print('Datos incorrectos(Revise el tipo y largo).')
                    continue
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue

                print(err)
                print('\n' * 20)
                continue

        elif opcion == '4':

            try:
                nombre = input('Ingrese el nombre del producto: ')
                query = """DELETE FROM producto WHERE nombre_producto = %s;"""

                datos = (nombre,)

                conexion(query, datos, 4)
                print('\n' * 20)
                print('El Producto a sido eliminado con exito.')

            except mysql.connector.Error as err:
                if err.errno == errorcode.WARN_DATA_TRUNCATED:
                    print('\n' * 20)
                    print('Datos incorrectos(Revise el tipo y largo).')
                    continue
                if err.errno == errorcode.ER_TRUNCATED_WRONG_VALUE:
                    print('\n' * 20)
                    print('Datos incorrectos(Revise el tipo y largo).')
                    continue
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue

                print(err)
                print('\n' * 20)
                continue

        elif opcion == '5':
            try:
                resultado = unidades_vendidas()
                formateador(resultado)
                print('\n' * 20)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue
        elif opcion == '6':
            try:
                resultado = productos_vendidos_x_mes()
                formateador(resultado)
                print('\n' * 20)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue
        elif opcion == '7':
            try:
                resultado = ventas_por_empleado()
                formateador(resultado)
                print('\n' * 20)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue
        elif opcion == '8':
            try:
                resultado = ventas_x_mes()
                formateador(resultado)
                print('\n' * 20)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n' * 20)
                    print('No existe la BD a la cual se quiere conectar.')
                    continue
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n' * 20)
                    print('El usuario o la contraseña con la que se conecta a la BD es incorrecta.')
                    continue

        elif opcion == '9':
            return

        else:
            print('\n' * 20)
            print('Opcion incorrecta')


if __name__ == '__main__':
    consultas()
