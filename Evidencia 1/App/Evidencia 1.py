

def login(credenciales: dict):
    """
    Se solicitan y validan las credenciales necesarias para ingresar al sistema.

    Parametros
        credenciales [dict] : Credenciales necesarias para comprobar la identidad del usuario.

    """
    intentos = 0
    while intentos < 4:

        # Se solicitan los datos.

        print('=' * 20)

        nombre_usuario = input('Ingrese su nombre de usuario: ')
        contraseña = input('Ingrese su contraseña: ')

        print('=' * 20)
        print('\n')

        # Se comprueba su validez.

        try:
            if credenciales[nombre_usuario]['contraseña'] == contraseña:
                print('\nSesion iniciada correctamente....')
                break
            else:
                intentos += 1
                print('\033[1;31m ')  # Colorea de rojo las letras de la consola
                print(f'Contraseña incorrecta.... Te quedan {4 - intentos} intentos.')
                print('\033[0;57m ')  # Vuelve al color blanco
        except KeyError:
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'Usuario incorrecto....')
            print('\033[0;57m ')  # Vuelve al color blanco
            print('\n')


def nuevo_usuario(credenciales: dict):
    """
    Se solicitan y verifican los datos necesarios para registrar un usuario. Si todos los datos
    son correctos se agrega un nuevo diccionario a la lista credenciales.

    """
    # Se solicitan los datos del nuevo usuario

    dni = input('Ingrese su Dni: ')
    nombre_real = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    correo = input('Ingrese su correo electronico: ')
    fecha_nac = input('Ingrese su fecha de nacimiento: ')

    # Se verifica que el nombre de usuario cumpla las condiciones.
    while True:
        print('=' * 20)
        nombre_usuario = input('Ingrese su nombre de usuario ( Entre 6 a 12 caracteres): ')

        # Se verifica si la longitud del nombre es correcta
        if len(nombre_usuario) > 12 or len(nombre_usuario) < 6:
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'El nombre de usuario debe tener entre 6 a 12 caracteres')
            print('\033[0;57m ')  # Vuelve al color blanco
            continue

        # Se verifica si el nombre de usuario es unico
        if nombre_usuario in credenciales.keys():
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'El nombre de usuario ya existe.')
            print('\033[0;57m ')  # Vuelve al color blanco
            continue
        else:
            break

    # Se verifica que la contraseña cumpla las condiciones solicitadas.
    while True:

        print('\033[1;31m ')  # Colorea de rojo las letras de la consola
        print(f'La contraseña debe cumplir al menos dos de las siguientes condiciones: '
              f'\n- Al menos un numero.'
              f'\n- Al menos una letra mayuscula.'
              f'\n- Al menos una letra minuscula.'
              f'\n- Al menos un caracter especial.')
        print('\033[0;57m ')  # Vuelve al color blanco

        contraseña = input('Ingrese su contraseña ( Debe contener minimo 8 caracteres): ')

        # Se verifica si la contraseña tiene la longitud correcta
        if len(contraseña) < 8:
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'La contraseña debe contener al menos 8 caracteres')
            print('\033[0;57m ')  # Vuelve al color blanco
            continue

        if contraseña.isupper() and contraseña.isalpha():
            print('Contraseña invalida. Verifique si cumple los requisitos.')
            print('=' * 20)
            print('\n')
            continue
        elif contraseña.islower() and contraseña.isalpha():
            print('Contraseña invalida. Verifique si cumple los requisitos.')
            print('=' * 20)
            print('\n')
            continue
        elif contraseña.isnumeric():
            print('Contraseña invalida. Verifique si cumple los requisitos.')
            print('=' * 20)
            print('\n')
            continue
        elif not (any(car.isdigit() for car in contraseña)):
            print('Contraseña invalida. Verifique si cumple los requisitos.')
            print('=' * 20)
            print('\n')
            continue
        else:
            break

    credenciales[nombre_usuario] = {'nombre_real': nombre_real,
                                    'contraseña': contraseña,
                                    'apellido': apellido,
                                    'correo': correo,
                                    'dni': dni,
                                    'fecha_nac': fecha_nac}

    return credenciales


def nueva_contra():
    pass


def menu():
    credenciales = {'admin': {'nombre_real': 'admin', 'contraseña': '1234', 'apellido': 'x'}}

    n = '\nSeleccione una opcion: '

    while True:
        print('\n' * 10)
        print("""
            
        ██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████  
        ██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██ 
        ██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██ 
        ██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██ 
        ██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████    
                                                                             
            """)

        print('\n 1- Inicie sesion.')
        print('\n 2- Registrate.')
        print('\n 3- ¿Olvido su contraseña?.')
        print('\n 4- Salir.')
        opcion = input(n)

        if opcion == '1':
            login(credenciales)
        elif opcion == '2':
            nuevo_usuario(credenciales)
        elif opcion == '3':
            pass
        elif opcion == '4':
            break
        else:
            n += '(Opcion invalida.......)\n'


if __name__ == "__main__":
    menu()
