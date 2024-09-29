from clases import *


def main():
    while True:
        print(f'==========Menu principal===========')
        print(f'1. Registrar Usuario.')
        print(f'2. Modificar Usuario.')
        print(f'3. Eliminar Usuario.')
        print(f'4. Buscar Usuario.')
        print(f'5. Mostrar Usuarios.')
        print(f'6. Log in.')
        print(f'7. Salir.')
        opcion = input('Ingrese una opcion: \n')
        if opcion == '1':
            datos_usuario = Usuario.solicitar_datos()
            Usuario.RegistrarUsuario(datos_usuario)
        elif opcion == '2':
            Usuario.ModificarUsuario()
        elif opcion == '3':
            username = input('Ingrese el nombre de usuario: ')
            Usuario.EliminarUsuario(username)
        elif opcion == '4':
            username = input('Ingrese el nombre de usuario: ')
            user = Usuario.BuscarUsuario(username)
            if user is None:
                print('El usuario no existe....')
                continue
            print('Los datos del usuario son: ')
            print(user, '\n')
            volver = input('Presione enter para volver al menu principal.....')
        elif opcion == '5':
            Usuario.MostrarUsuarios()
        elif opcion == '6':
            user = Usuario.LogearUsuario()
        elif opcion == '7':
            print('Que tenga buen dia.....')
            Acceso.MostrarAccesos()
            return
        else:
            print('Opcion incorrecta.')


if __name__ == '__main__':
    main()

