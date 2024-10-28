from gestion_de_archivos import *
import datetime


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

        return accesos
