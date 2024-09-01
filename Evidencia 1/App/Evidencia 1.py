

def login(credenciales: list[dict]):
    """
    Se solicitan y validan las credenciales necesarias para ingresar al sistema.

    Parametros
        credenciales [list] : Credenciales necesarias para comprobar la identidad del usuario.

    """
    intentos = 0
    while intentos < 4:

        # Se solicitan los datos.
        print('=' * 20)
        nombre_usuario = input('Ingrese su nombre de usuario: ')
        contraseña = int(input('Ingrese su contraseña: '))
        print('=' * 20)
        print('\n')

        # Se comprueba su validez.
        for usuario in credenciales:
            if usuario['nombre'] == nombre_usuario and usuario['contraseña'] == contraseña:
                print('\nSesion iniciada correctamente....')
                intentos = 5
                break
            elif usuario['nombre'] == nombre_usuario and usuario['contraseña'] != contraseña:
                intentos += 1
                print('\033[1;31m ')  # Colorea de rojo las letras de la consola
                print(f'Contraseña incorrecto.... Te quedan {intentos} intentos.')
                print('\033[0;57m ')  # Vuelve al color blanco
                break
        else:
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'Usuario incorrecto....')
            print('\033[0;57m ')  # Vuelve al color blanco
            print('\n')


def nuevo_usuario(credenciales: list[dict]):
    """
    Se solicitan y verifican los datos necesarios para registrar un usuario. Si todos los datos
    son correctos se agrega un nuevo diccionario a la lista credenciales.

    """
    while True:
        print('=' * 20)
        nombre = input('Ingrese su nombre de usuario ( Entre 6 a 12 caracteres): ')

        # Se verifica si la longitud del nombre es correcta
        if len(nombre) > 12 or len(nombre) < 6:
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'El nombre de usuario debe tener entre 6 a 12 caracteres')
            print('\033[0;57m ')  # Vuelve al color blanco
            continue

        # Se verifica si el nombre de usuario es unico
        existe = False
        for usuario in credenciales:
            if usuario['nombre'] == nombre:
                print('\033[1;31m ')  # Colorea de rojo las letras de la consola
                print(f'El nombre de usuario ya existe.')
                print('\033[0;57m ')  # Vuelve al color blanco
                existe = True
                break
        if existe:
            continue

    while True:
        contraseña = input('Ingrese su contraseña ( Debe contener minimo 8 caracteres):: ')

        # Se verifica si la contraseña tiene la longitud correcta
        if len(contraseña) < 8:
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'La contraseña debe contener al menos 8 caracteres')
            print('\033[0;57m ')  # Vuelve al color blanco
            continue

        condiciones = 0

        # Se comprueba que tenga algun numero
        if contraseña.isalnum():
            condiciones += 1

        # Se verifica si tiene al menos una mayuscula
        if contraseña.isupper():
            condiciones += 1
        # Se verifica si tiene al menos una minuscula
        elif contraseña.islower():
            condiciones += 1
        # Verdadero si tiene mayusculas y minusculas
        elif not contraseña.isnumeric():
            condiciones += 2

        if condiciones < 2:
            print('\033[1;31m ')  # Colorea de rojo las letras de la consola
            print(f'La contraseña debe cumplir al menos dos de las siguientes condiciones: '
                  f'- Al menos un numero.'
                  f'- Al menos una letra mayuscula.'
                  f'- Al menos una letra minuscula.'
                  f'- Al menos un caracter especial.')
            print('\033[0;57m ')  # Vuelve al color blanco

        print('=' * 20)
        print('\n')

    dni = input('Ingrese su Dni: ')
    nombre_real = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    correo = input('Ingrese su correo electronico: ')
    fecha_nac = input('Ingrese su fecha de nacimiento: ')

    credenciales.append({'nombre': nombre, 'contraseña': contraseña})
    return credenciales


def nueva_contra():
    pass


def menu():
    credenciales = [{'nombre': 'admin', 'contraseña': 1234}]

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
