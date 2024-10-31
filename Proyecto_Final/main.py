try:

    from clase_usuario import *
    from clase_acceso import *
    from gestion_de_archivos import *
    from Consultas import *
    from Carga_Grafico_Registros_Pluviales import registros_pluviales

except ModuleNotFoundError as err:
    from clase_usuario import *
    from clase_acceso import *
    from gestion_de_archivos import *
    from Carga_Grafico_Registros_Pluviales import registros_pluviales

    print('No posee el modulo MySQL')

def crud_users():
    """
    Se muestra el menú para realizar un CRUD al usario y
    se toman los datos para realizarlo.

    """
    while True:
        print('=' * 15)
        print('1. Agregar un nuevo usuario.')
        print('2. Modificar un usuario.')
        print('3. Eliminar un usuario.')
        print('4. Volver al menú principal.')
        print('=' * 15)

        opcion = input('Ingrese su opcion: ')

        if opcion == '1':

            limpiar_consola()
            while True:
                try:

                    nw_user = Usuario()
                    nw_user.username = input('\nIngrese el nombre del usuario: ')
                    nw_user.password = input('Ingrese la contraseña del usuario: ')
                    nw_user.email = input('Ingrese el email del usuario: ')
                    nw_user.DNI = input('Ingrese el DNI del usuario: ')
                    nw_user.RegistrarUsuario()
                    break
                except Exception as err:

                    limpiar_consola()
                    print(err)
            limpiar_consola()
            print('Usuario registrado con exito.')

        elif opcion == '2':
            while True:

                username = input('Ingrese el nombre de usuario a modificar: ')

                try:

                    Usuario.ModificarUsuario(username)
                    limpiar_consola()
                    print('Usuario modificado con exito.')
                    break

                except Exception as err:
                    limpiar_consola()
                    print(err)

        elif opcion == '3':
            opcion = input('Eliminar por 1- usuario o 2- email: ')

            if opcion == '1':
                username = input('Ingrese el username: ')

                try:
                    Usuario.EliminarUsuario(username=username)
                    limpiar_consola()
                    print('Usuario eliminado con exito.')
                except Exception as err:
                    limpiar_consola()
                    print(err)

            elif opcion == '2':
                email = input('Ingrese el email: ')

                try:
                    Usuario.EliminarUsuario(email=email)
                    limpiar_consola()
                    print('Usuario eliminado con exito.')
                except Exception as err:
                    limpiar_consola()
                    print(err)
            else:
                print('Opcion incorrecta..')

        elif opcion == '4':
            limpiar_consola()
            return
        else:
            limpiar_consola()
            print('Opcion incorrecta.....')


def acces_data():

    while True:

        print('=' * 15)
        print('1. Mostrar los Accesos (datos de accesos.ispc)')
        print('2. Mostrar los logs de intentos fallidos (datos de logs.txt)')
        print('3. Volver al menú principal. ')

        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            limpiar_consola()
            accesos = Acceso.MostrarAccesos()

            if accesos is None:
                print("Error: 'accesos' es None")
                return
            for i in accesos:
                print(i)
            continuar = input('\nPresione enter para continuar...')
            limpiar_consola()

        elif opcion == '2':
            limpiar_consola()
            mostrar_logs()
            continuar = input('\nPresione enter para continuar...')
            limpiar_consola()

        elif opcion == '3':
            limpiar_consola()
            return

        else:
            print('Opcion incorrecta.')
            limpiar_consola()


def ordenamiento_y_busqueda():
    while True:
        print('=' * 15)
        print('1. Ordenar usuarios por username.')
        print('2. Búsqueda  de usuario por DNI.')
        print('3. Búsqueda  de usuario por USERNAME.')
        print('4. Búsqueda  de usuario por EMAIL.')
        print('5. Mostrar todos los usuarios.')
        print('6. Volver.')
        print('=' * 15)

        opcion = input('Ingrese su opcion: ')

        if opcion == '1':
            limpiar_consola()
            Usuario.ordenar()

        elif opcion == '2':

            limpiar_consola()
            dni = input('Ingrese el DNI del usuario a buscar: ')

            if not dni.isdigit():
                limpiar_consola()
                print('El DNI debe ser un numero.')
                continue

            Usuario.buscar_x_dni(int(dni))
            limpiar_consola()

        elif opcion == '3':
            limpiar_consola()
            nombre = input('Ingrese el nombre del usuario a buscar: ')

            Usuario.BuscarUsuario(nombre)
            limpiar_consola()

        elif opcion == '4':
            limpiar_consola()
            email = input('Ingrese el email del usuario: ')

            Usuario.buscar_x_email(email)
            limpiar_consola()
        elif opcion == '5':
            print('\n' * 20)
            Usuario.MostrarUsuarios()
            limpiar_consola()
        elif opcion == '6':
            return
        else:
            limpiar_consola()
            print('Opcion incorrecta...')


def limpiar_consola():

    print('\n' * 20)


def menu_principal():

    while True:

        print('=' * 15)
        print('1. Usuarios y Accesos de la Aplicación.')
        print('     a. Acceder al CRUD de los Usuarios en POO.')
        print('     b. Mostrar los datos de Accesos.')
        print('     c. Ordenamiento y Búsqueda de usuarios.')
        print('     d. Volver al Menú principal.')
        print('2. Ingresar al sistema con los datos de usuario.')
        print('     a. Gestión de la Base de Datos.')
        print('     b. Volver al Menú principal.')
        print('     c. Salir de la aplicación.')
        print('3. Análisis de datos.')
        print('4. Salir de la aplicación.')
        print('=' * 15)

        opcion = input('Ingrese una opcion del menú principal:  ')

        if opcion == '1':

            opcion = input('Ingrese una opcion del submenú: ')

            if opcion == 'a':
                limpiar_consola()
                crud_users()

            elif opcion == 'b':
                limpiar_consola()
                acces_data()

            elif opcion == 'c':
                limpiar_consola()
                ordenamiento_y_busqueda()

            elif opcion == 'd':
                print('Volviendo.....')
                limpiar_consola()

            else:
                limpiar_consola()
                print('Opcion incorrecta.....')

            limpiar_consola()

        elif opcion == '2':
            limpiar_consola()
            Usuario.LogearUsuario()
            try:
                consultas()
            except NameError as err:
                print('No posee instalado el conector a MySql. Instalelo para poder acceder a esta funcionalidad.')
                seguir = input('\nPresione enter para continuar...')
            limpiar_consola()

        elif opcion == '3':
            limpiar_consola()
            registros_pluviales()

        elif opcion == '4':
            print('Vuelva pronto......')
            return

        else:
            limpiar_consola()
            print('Opcion incorrecta')


if __name__ == '__main__':
    menu_principal()
