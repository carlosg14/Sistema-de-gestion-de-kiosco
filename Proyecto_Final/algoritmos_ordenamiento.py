import os.path

from gestion_de_archivos import *
from  datetime import  datetime

def insertionSort(lista: list[object]):
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


def busqueda_binaria(lista: list[object], buscado, criterio, tipo, archivo):


    if not os.path.exists('./búsquedasYordenamientos'):
        os.mkdir('./búsquedasYordenamientos')
    ahora = str(datetime.now()).replace(':', '-')
    inicio = 0
    final = len(lista) - 1
    contador = 1
    log = (f'Búqueda binaria por {tipo}: buscando {tipo} {buscado}.'
           f' \nen el archivo {archivo} que contiene {len(lista)} usuarios.')

    if criterio(lista[final]) < buscado:
        log += (f'\nNo se encuentra registrado el usuario con ese {tipo} debido a que '
                f'\nel {tipo} a buscar es más grande que el más grande de los registrados')
        busqueda_bin_log(f'búsquedasYordenamientos/buscandoUsuarioPor{tipo}-{ahora}.txt ', log)
        return None

    if criterio(lista[inicio]) > buscado:
        log += (f'\nNo se encuentra registrado el usuario con ese {tipo} debido a que '
                f'\nel {tipo} a buscar es más chico que el más chico de los registrados')
        busqueda_bin_log(f'búsquedasYordenamientos/buscandoUsuarioPor{tipo}-{ahora}.txt ', log)
        return None

    while inicio <= final:
        medio = (inicio + final) // 2
        if criterio(lista[medio]) == buscado:
            log += (f'\nIntento {contador}: {tipo} del usuario de la posicion {medio} es {criterio(lista[medio])}'
                    f'\npor lo tanto se encontró el usuario en {contador} intentos')
            busqueda_bin_log(f'búsquedasYordenamientos/buscandoUsuarioPor{tipo}-{ahora}.txt ', log)
            return lista[medio]
        elif criterio(lista[medio]) < buscado:
            log += (f'\nIntento {contador}: {tipo} del usuario de la posicion {medio} es {criterio(lista[medio])}'
                    f'\npor lo tanto se buscará en la subsecuencia de la derecha ({tipo} más grandes) (posición {medio + 1} a {final + 1})')
            inicio = medio + 1
        else:
            log += (f'\nIntento {contador}: {tipo} del usuario de la posicion {medio} es {criterio(lista[medio])}'
                    f'\npor lo tanto se buscará en la subsecuencia de la derecha ({tipo} más chicos) (posición {inicio} a {medio - 1})')
            final = medio - 1
        contador += 1
    log += f'\n Se realizaron {contador - 1} intentos y no se encontró el {tipo} buscado, no está registrado.'
    busqueda_bin_log(f'búsquedasYordenamientos/buscandoUsuarioPor{tipo}-{ahora}.txt ', log)
    return None
