import datetime
import pickle


class Usuario:

    users_file = 'usuarios.ispc'
    ordenado = False


    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f'- id: {self.id} | username: {self.username} | password: {self.password} | email: {self.email}'


    @classmethod
    def solicitar_datos(cls) -> tuple:
        """
        Solicita los datos necesarios para crear y registrar un nuevo usuario.
        Ademas verifica que esos datos ya no existan.

        RETURN : Retorna una tupla con los datos del nuevo usuario.
        """
        # Se verifica que el nombre de usuario sea unico.
        while True:
            username = input('Ingrese el nombre de usuario: ')
            if cls.BuscarUsuario(username) is None:
                break
            print('Ese nombre de usuario ya existe. Elija otro por favor. ')

        password = input('Ingrese su contraseña: ')
        email = input('Ingrese su email: ')

        nuevo_user = (0, username, password, email)
        return nuevo_user

    @classmethod
    def RegistrarUsuario(cls, user_data: tuple):
        """
        Registra un objeto usuario en el archivo binario usuarios.ispc

        """
        # Se leen los usuarios del archivo.
        usuarios = leer_binario(cls.users_file)

        # Se agrega el nuevo usuario
        if usuarios is None:
            nuevo_usario = cls(user_data[0] + 1, user_data[1], user_data[2], user_data[3])
            usuarios = [nuevo_usario]
        else:
            nuevo_usario = cls(usuarios[-1].id + 1, user_data[1], user_data[2], user_data[3])
            usuarios.append(nuevo_usario)

        # Se guardan los usuarios
        escribir_binario(cls.users_file, usuarios)
        cls.ordenado = False
        print('Usuario registrado con exito...')

    @classmethod
    def ModificarUsuario(cls):
        """
        Esta funcion permite modificar los datos de un usuario.

        """
        # Se solicita el nombre del usuario a modifcar
        username = input('Ingrese el nombre de usuario a modificar: ')

        # Se verifica si existe
        user_data = cls.BuscarUsuario(username)

        if user_data is None:
            print('El usuario no existe....')
            return

        usuarios = leer_binario(cls.users_file)
        correcta = False
        # Se solicitan los nuevos datos.
        while not correcta:
            nw_username = input('Ingrese el nuevo nombre de usuario: ')
            for user in usuarios:
                if user.username == nw_username and user.username != username:
                    print('Ese nombre de usuario ya existe. Elija otro por favor. ')
                    break
            else:
                correcta = True
        nw_password = input('Ingrese su nueva contraseña: ')
        nw_email = input('Ingrese el nuevo email: ')

        for user in usuarios:
            if user.username == username:
                user.username = nw_username
                user.password = nw_password
                user.email = nw_email

        escribir_binario(cls.users_file, usuarios)
        cls.ordenado = False

        print('Usuario modificado con exito...')

    @classmethod
    def EliminarUsuario(cls, username):
        """
        Elimina un usuario.

        """
        usuarios = leer_binario(cls.users_file)

        try:
            for user in usuarios:
                if user.username == username:
                    usuarios.remove(user)
                    escribir_binario(cls.users_file, usuarios)
                    print('Usuario eliminado con exito....')
                    return
            print('El usuario no existe..')
        except TypeError:
            print('No hay usuarios registrados ...\n')
            return


    @classmethod
    def BuscarUsuario(cls, username) -> object:
        """
        Busca un usuario por nombre.

        Returns:
            [None] : En caso de que el usuario no exista.

        """
        usuarios = leer_binario(cls.users_file)

        if not usuarios:
            return None
        if not cls.ordenado:
            for user in usuarios:
                if user.username == username:
                    print('Busqueda realizada de forma secuencial.')
                    return user
        else:
            usuario = busqueda_binaria(usuarios, username)
            print('Busqueda realizada usando la busqueda binaria.')
            return usuarios[usuario]
    @classmethod
    def MostrarUsuarios(cls):
        """
        Muestra todos los usuarios registrados.

        """
        usuarios = leer_binario(cls.users_file)

        try:
            for user in usuarios:
                print(user)
            volver = input('\nPresione enter para volver al menu principal.....')

        except TypeError:
            print('No hay usuarios registrados ...')

    @classmethod
    def LogearUsuario(cls):
        """
        Se solicitan y validan las credenciales necesarias para ingresar al sistema.

        """
        while True:
            username = input('Ingrese su nombre de usuario: ')
            password = input('Ingrese su contraseña: ')
            user_data = cls.BuscarUsuario(username)
            if user_data is None:
                print('Usuario no encontrado....')
                registrar_log(username, password)

                continue

            if password == user_data.password:
                fecha_ingreso = datetime.datetime.now()
                print("""

                        ██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████  
                        ██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██ 
                        ██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██ 
                        ██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██ 
                        ██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████    

                            """)
                volver = input('Presione enter para volver al menu principal.....')
                Acceso.RegistrarAcceso(username, fecha_ingreso)
                return
            print('Contraseña incorrecta.....')
            registrar_log(username, password)

    @classmethod
    def ordenar(cls):
        """
        Ordena a los usuarios por nombre,
        a traves del metodo de la insercion o el metodo sort de python

        """
        print('=' * 5)
        print('1. Ordenar por metodo de la insercion.')
        print('2. Ordenar por metodo sort de python.')
        print('3. Salir.')
        print('=' * 5)
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            usuarios = leer_binario(cls.users_file)
            users_sorted = insertionSort(usuarios)
            escribir_binario(cls.users_file, users_sorted)
            cls.ordenado = True
        elif opcion == '2':
            usuarios = leer_binario(cls.users_file)
            usuarios.sort(key=lambda user: user.username)
            escribir_binario(cls.users_file, usuarios)
            cls.ordenado =  True
        elif opcion == '3':
            return
        else:
            print('Opcion incorrecta.')




class Acceso:

    acces_file = 'accesos.ispc'

    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogeado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogeado = usuarioLogeado

    def __str__(self):
        return f'- id: {self.id} | usuario: {self.usuarioLogeado} | Ingreso: {self.fechaIngreso} | Salida: {self.fechaSalida}'
    @classmethod
    def RegistrarAcceso(cls, username, ingreso):
        accesos = leer_binario(cls.acces_file)


        if accesos is None:
            accesos = [cls(0, ingreso, datetime.datetime.now(), username)]
        else:
            accesos.append(cls(accesos[-1].id + 1, ingreso, datetime.datetime.now(), username))

        escribir_binario(cls.acces_file, accesos)

    @classmethod
    def MostrarAccesos(cls):
        accesos = leer_binario(cls.acces_file)

        for acceso in accesos:
            print(acceso)

def leer_binario(archivo) -> list[Usuario] | None:
    """
    Lee el archivo binario que se pasa por parametro. Devuelve NONE si el archivo no existe.

    """
    try:
        file = open(archivo, 'rb')
        usuarios = pickle.load(file)
        file.close()
        return usuarios
    except IOError:
        return None


def escribir_binario(archivo, objeto=None):
    """
    Escribe el archivo que se recibe por parametro con lo especificado en el parametro objeto.

    """

    file = open(archivo, 'wb')
    pickle.dump(objeto, file)
    file.close()



def registrar_log(username, password):
    """
    Escribe en un archivo de texto un log con el siguiente formato:
    | Fecha actual | Nombre de usuario | Contraseña |

    """
    file = open('logs.txt', 'a')
    log = f'|{datetime.datetime.now()}| usuario: {username} | clave: {password}\n'
    file.write(log)
    file.close()


def insertionSort(lista: list[Usuario]):
    n = len(lista)

    if n <= 1:
        return

    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and key.username < lista[j].username:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

    return lista


def busqueda_binaria(lista: list[Usuario], buscado: str):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio].username == buscado:
            return medio
        elif lista[medio].username < buscado:
            inicio = medio + 1
        else:
            final = medio - 1

    return None