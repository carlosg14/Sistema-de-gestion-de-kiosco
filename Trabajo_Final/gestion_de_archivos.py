import datetime
import pickle


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
    except Exception as err:
        print(err)


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


def mostrar_logs():

    file = open('logs.txt', 'rt')

    print(file.read())


def busqueda_bin_log(archivo, txt):
    """
    Crea los archivos de log para los distintos tipos de busqueda binaria

    """
    file = open(archivo, 'x')
    file.write(txt)
    file.close()

