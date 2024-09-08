import datetime
import random
import time

from aritmetica import *


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
                registrar_ingreso(nombre_usuario)
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

    # Se verifica que el nombre de usuario sea valido.
    while True:
        print('=' * 20)
        nombre_usuario = input('Ingrese su nombre de usuario ( Entre 6 a 12 caracteres): ')

        valido = valid_user(nombre_usuario, credenciales)
        if valido:
            break

    # Se verifica que la contraseña sea valida.
    while True:

        print('\033[1;31m ')  # Colorea de rojo las letras de la consola
        print(f'La contraseña debe cumplir al menos dos de las siguientes condiciones: '
              f'\n- Al menos un numero.'
              f'\n- Al menos una letra mayuscula.'
              f'\n- Al menos una letra minuscula.'
              f'\n- Al menos un caracter especial.')
        print('\033[0;57m ')  # Vuelve al color blanco

        contraseña = input('Ingrese su contraseña ( Debe contener minimo 8 caracteres): ')

        valida = valid_passw(contraseña)

        if valida:
            break

    # Se verifica si es un humano.
    while True:
        humano = is_human()
        if humano:
            break
        print('1- Continuar.')
        print('2- Salir del registro.')
        continuar = input('Ingrese su opcion: ')
        if continuar == '2':
            return

    credenciales[nombre_usuario] = {'nombre_real': nombre_real,
                                    'contraseña': contraseña,
                                    'apellido': apellido,
                                    'correo': correo,
                                    'dni': dni,
                                    'fecha_nac': fecha_nac}

    save_user(credenciales[nombre_usuario], nombre_usuario)
    return credenciales


def save_user(datos, usuario):
    """
    Se guardan los datos del usuario en el archivo usuariosCreados.txt.

    Parametros

        datos [dict]: Datos del usuario.
        usuario [str]: Nombre del usuario.

    """

    datos = [value + ',' for value in datos.values()]
    try:
        with open('usuariosCreados.txt', 'xt') as archivo:
            archivo.write('Nombre de usuario, Nombre real, Contraseña, Apellido, Correo, Dni, Fecha_nac\n')
            archivo.write(usuario + ',')
            archivo.writelines(datos)
            archivo.write('\n')
    except FileExistsError:
        with open('usuariosCreados.txt', 'at') as archivo:
            archivo.write(usuario + ',')
            archivo.writelines(datos)
            archivo.write('\n')


def registrar_ingreso(user):
    try:
        with open('ingresos.txt', 'xt') as archivo:
            archivo.write(f'{datetime.datetime.now()} : Ingreso el usuario {user}.')

    except FileExistsError:
        with open('ingresos.txt', 'at') as archivo:
            archivo.write(f'{datetime.datetime.now()} : Ingreso el usuario {user}.')


def nueva_contra():
    pass


def is_human():
    """
    Devuelve True si resuleve el CAPTCHA correctamente, False en caso contrario.

    """
    # Se generan los numeros aleatorios

    a = random.randint(a=0, b=10)
    b = random.randint(a=0, b=10)
    operacion = random.randint(a=1, b=4)

    if operacion == 1:
        resultado = sumar(a, b)
        print('Cual es el resultado de la siguiente operacion: '
              f'{a} + {b} = ...')
    elif operacion == 2:
        resultado = restar(a, b)
        print('Cual es el resultado de la siguiente operacion: '
              f'{a} - {b} = ...')
    elif operacion == 3:
        resultado = multiplicar(a, b)
        print('Cual es el resultado de la siguiente operacion: '
              f'{a} * {b} = ...')
    else:
        resultado = dividir(a, b)
        print('Cual es el resultado de la siguiente operacion: '
              f'{a} / {b} = ...')
    respuesta = float(input('Respuesta (Debe contener maximo dos numeros decimales): '))
    if resultado == respuesta:
        print('Resultado correcto.')
        return True
    print('Resultado incorrecto.')
    return False


def valid_passw(cadena: str):
    """
    Retorna True si cadena tiene 8 o mas caracteres y cumple 2 de las siguientes condiciones:
      - Al menos un numero.
      - Al menos una letra mayuscula.
      - Al menos una letra minuscula.
      - Al menos un caracter especial.
    Retoran False en caso contrario.

    Parametros
     cadena [str]

    """
    if len(cadena) < 8:
        print('\033[1;31m ')  # Colorea de rojo las letras de la consola
        print(f'La contraseña debe contener al menos 8 caracteres')
        print('\033[0;57m ')  # Vuelve al color blanco
        return False
    if cadena.isupper() and cadena.isalpha():
        print('Contraseña invalida. Verifique si cumple los requisitos.')
        print('=' * 20)
        print('\n')
        return False
    elif cadena.islower() and cadena.isalpha():
        print('Contraseña invalida. Verifique si cumple los requisitos.')
        print('=' * 20)
        print('\n')
        return False
    elif cadena.isnumeric():
        print('Contraseña invalida. Verifique si cumple los requisitos.')
        print('=' * 20)
        print('\n')
        return False
    elif not (any(car.isdigit() for car in cadena)):
        print('Contraseña invalida. Verifique si cumple los requisitos.')
        print('=' * 20)
        print('\n')
        return False

    return True


def valid_user(nombre_usuario: str, credenciales: dict):
    """
    Devuelve True si esl nombre de usuario es unico y si su longitud esta entre 6 a 12 caracteres.

    Parametros:
     cadena [str]
     credenciales [dict]

    """
    if len(nombre_usuario) > 12 or len(nombre_usuario) < 6:
        print('\033[1;31m ')  # Colorea de rojo las letras de la consola
        print(f'El nombre de usuario debe tener entre 6 a 12 caracteres')
        print('\033[0;57m ')  # Vuelve al color blanco
        return False

    # Se verifica si el nombre de usuario es unico
    if nombre_usuario in credenciales.keys():
        print('\033[1;31m ')  # Colorea de rojo las letras de la consola
        print(f'El nombre de usuario ya existe.')
        print('\033[0;57m ')  # Vuelve al color blanco
        return False

    return True


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
