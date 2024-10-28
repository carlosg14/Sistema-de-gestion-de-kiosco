from gestion_de_archivos import *
import datetime
from clase_acceso import *
from algoritmos_ordenamiento import *

class Usuario:

    users_file = 'usuarios.ispc'


    def __init__(self, id=None, DNI=None, username=None, password=None, email=None):
        self._id = id
        self._username = username
        self._password = password
        self._email = email
        self._DNI = DNI

    def __str__(self):
        return f'- id: {self._id} | username: {self._username} | password: {self._password} | email: {self._email}| DNI: {self._DNI}'


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def DNI(self):
        return self._DNI

    @DNI.setter
    def DNI(self, value: str):
        if not value.isdigit():
            raise Exception('El campo DNI debe estar compuesto por numeros.')
        self._DNI = int(value)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
       return self._password

    @password.setter
    def password(self, value):
        self._password = value


    def RegistrarUsuario(self):
        """
        Registra un objeto usuario en el archivo binario usuarios.ispc

        """
        if self.BuscarUsuario(self.username):
            raise Exception('El nombre de usuario ya existe.')

        # Se leen los usuarios del archivo.
        usuarios = leer_binario(self.users_file)

        # Se agrega el nuevo usuario
        if usuarios is None:
            self.id = 1
            usuarios = [self]
        else:
            usuarios.sort(key=lambda x: x.id)
            self.id = usuarios[-1].id + 1
            usuarios.append(self)
            usuarios.sort(key=lambda x: x.DNI)

        # Se guardan los usuarios
        escribir_binario(self.users_file, usuarios)
        if not (leer_binario('usuariosOrdenadosPorUsername.ispc') is None):
            escribir_binario('usuariosOrdenadosPorUsername.ispc', usuarios.sort(key=lambda x: x.username))

        print('Usuario registrado con exito...')

    @classmethod
    def ModificarUsuario(cls, username):
        """
        Esta funcion permite modificar los datos de un usuario.

        """

        # Compobamos si el usuario existe
        if cls.BuscarUsuario(username) is None:
            raise Exception(f'No existe el usuario {username}')

        usuarios: list[Usuario] = leer_binario(cls.users_file)

        # Se solicitan los nuevos datos.

        for user in usuarios:
            if user.username == username:
                user.username = input('Ingrese el nuevo nombre de usuario: ')
                user.password = input('Ingrese su nueva contraseña: ')
                user.email = input('Ingrese el nuevo email: ')
                user.DNI = input('Ingrese su nuevo DNI: ')
                break
        existe = cls.BuscarUsuario(user.username)
        if existe and existe.username != username:
            raise Exception('El nuevo nombre de usuario ya exite..')

        escribir_binario(cls.users_file, usuarios)
        if not (leer_binario('usuariosOrdenadosPorUsername.ispc') is None):
            escribir_binario('usuariosOrdenadosPorUsername.ispc', usuarios.sort(key=lambda x: x.username))

        print('Usuario modificado con exito...')

    @classmethod
    def EliminarUsuario(cls, username=None, email=None):
        """
        Elimina un usuario.

        """
        usuarios: list[Usuario] = leer_binario(cls.users_file)

        if not usuarios:
            raise Exception('No hay usuarios registrados.')

        for user in usuarios:
            if user.username == username or user.email == email:
                usuarios.remove(user)
                escribir_binario(cls.users_file, usuarios)
                print('Usuario eliminado con exito....')
                return

        raise Exception('El usuario no existe.')

    @classmethod
    def BuscarUsuario(cls, username):
        """
        Busca un usuario por nombre.

        Returns:
            [None] : En caso de que el usuario no exista.

        """
        usuarios = leer_binario('usuariosOrdenadosPorUsername.ispc')

        if not usuarios:
            usuarios = leer_binario(cls.users_file)

            if usuarios is None:
                print('No hay usuarios registrados')
                continuar = input('\nPresione enter para continuar....')
                print('\n' * 20)
                return

            contador = 1
            print(f'\nBuscando Username {username}.')
            for user in usuarios:
                if user.username == username:
                    print(f'Intento {contador}: {username} es igual a {user.username}')
                    print(user)
                    print('\nRealizado por busqueda secuencial.')
                    continuar = input('\nPresione enter para continuar....')
                    print('\n' * 20)
                    return user
                print(f'Intento {contador}: {username} es distinto de {user.username}')
                contador += 1
            print(f'No se pudo encontrar el usuario despues de {contador - 1} intentos.')
            print('\nRealizado por busqueda secuencial.')
            continuar = input('\nPresione enter para continuar....')
            print('\n' * 20)
            return
        user = busqueda_binaria(usuarios, username, lambda x: x.username, 'Username', 'usuariosOrdenadosPorUsername.ispc')

        if user is None:
            print('\nEl usuario no existe.')
            print('\nRealizado por busqueda binaria.')
            continuar = input('\nPresione enter para continuar....')
            print('\n' * 20)
            return

        print()
        print(user)
        print('\nRealizado por busqueda binaria.')
        continuar = input('\nPresione enter para continuar....')
        print('\n' * 20)
        return user

    @classmethod
    def buscar_x_dni(cls, dni):

        usuarios = leer_binario(cls.users_file)

        if not usuarios:
            return None

        user = busqueda_binaria(usuarios, dni, lambda x: str(x.DNI), 'DNI', cls.users_file)

        if user is None:
            print('\nEl usuario no existe.')
            print('\nSe utilizo la busqueda binaria. ')
            continuar = input('\nPresione enter para continuar....')
            return

        print()
        print(user)
        print('\nSe utilizo la busqueda binaria. ')
        continuar = input('\nPresione enter para continuar....')

    @classmethod
    def buscar_x_email(cls, email):

        usuarios = leer_binario(cls.users_file)

        if usuarios is None:
            print('\nNo hay usuarios registrados')
            continuar = input('\nPresione enter para continuar...')

        contador = 1
        print(f'\nBuscando Email {email}.')
        for user in usuarios:
            if user.email == email:
                print(f'Intento {contador}: {email} es igual a {user.email}')
                print(user)
                print('\nSe utilizo busqueda secuencial.')
                continuar = input('\nPresione enter para continuar...')
                return
            print(f'Intento {contador}: {email} es distinto de {user.email}')
            contador += 1

        print(f'No se pudo encontrar el usuario despues de {contador - 1} intentos.')
        continuar = input('\nPresione enter para continuar...')

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
            user_data: Usuario = cls.BuscarUsuario(username)
            if user_data is None:
                print('Usuario no encontrado....')
                registrar_log(username, password)

                continue

            if password == user_data.password:
                print('\n' * 20)
                fecha_ingreso = datetime.now()
                print("""

                        ██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████  
                        ██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██ 
                        ██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██ 
                        ██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██ 
                        ██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████    

                            """)
                Acceso.RegistrarAcceso(username, fecha_ingreso)
                return
            print('Contraseña incorrecta.....')
            registrar_log(username, password)

    @classmethod
    def ordenar(cls):
        """
        Ordena a los usuarios por nombre.
        """

        usuarios = leer_binario(cls.users_file)
        users_sorted = insertionSort(usuarios)
        escribir_binario('usuariosOrdenadosPorUsername.ispc', users_sorted)
        print('Usuarios ordenados con exito.')




