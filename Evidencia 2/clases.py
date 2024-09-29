import datetime
import pickle


class Usuario:

    users_file = 'usuarios.ispc'

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f'- id: {self.id} | username: {self.username} | password: {self.password} | email: {self.email}'


    @classmethod
    def solicitar_datos(cls):
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
    def RegistrarUsuario(cls, user_data):
        """
        Registra un objeto usuario en el archivo binario usuarios.ispc

        """
        # Se leen los usuarios del archivo.
        usuarios = leer_binario(cls.users_file)

        # Se guardan los usuarios junto con el nuevo usuario
        if usuarios is None:
            nuevo_usario = cls(user_data[0] + 1, user_data[1], user_data[2], user_data[3])
            usuarios = [nuevo_usario]
        else:
            nuevo_usario = cls(usuarios[-1].id + 1, user_data[1], user_data[2], user_data[3])
            usuarios.append(nuevo_usario)

        escribir_binario(cls.users_file, usuarios)

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

        cls.EliminarUsuario(username)

        new_user_data = cls.solicitar_datos()

        usuarios = leer_binario(cls.users_file)

        user_data.username = new_user_data[1]
        user_data.password = new_user_data[2]
        user_data.email = new_user_data[3]

        usuarios.append(user_data)

        escribir_binario(cls.users_file, usuarios)

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

        try:
            for user in usuarios:
                if user.username == username:
                    return user

        except TypeError:
            return None

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
                file = open('logs.txt', 'a')
                log = f'|{datetime.datetime.now()}| usuario: {username} | clave: {password} \n'
                file.write(log)
                file.close()

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
            file = open('logs.txt', 'a')
            log = f'|{datetime.datetime.now()}| usuario: {username} | clave: {password}\n'
            file.write(log)
            file.close()




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

def leer_binario(archivo) -> list | None:
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