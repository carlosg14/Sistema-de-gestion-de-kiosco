import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

def obtener_registro_pluviales():

    try:
        datos = pd.read_csv('datos_pluviales.csv')
    except FileNotFoundError:
        enero = [random.randint(0, 100) for i in range(31)]
        febrero = [random.randint(0, 100) for i in range(28)] + [np.nan, np.nan, np.nan]
        marzo = [random.randint(0, 100) for i in range(31)]
        abril = [random.randint(0, 100) for i in range(30)] + [np.nan]
        mayo = [random.randint(0, 100) for i in range(31)]
        junio = [random.randint(0, 100) for i in range(30)] + [np.nan]
        julio = [random.randint(0, 100) for i in range(31)]
        agosto = [random.randint(0, 100) for i in range(31)]
        septiembre = [random.randint(0, 100) for i in range(30)] + [np.nan]
        octubre = [random.randint(0, 100) for i in range(31)]
        noviembre = [random.randint(0, 100) for i in range(30)] + [np.nan]
        diciembre = [random.randint(0, 100) for i in range(31)]
        año = {'enero': enero,
               'febrero': febrero,
               'marzo': marzo,
               'abril': abril,
               'mayo': mayo,
               'junio': junio,
               'julio': julio,
               'agosto': agosto,
               'septiembre': septiembre,
               'octubre': octubre,
               'noviembre': noviembre,
               'diciembre': diciembre,
               }
        datos = pd.DataFrame(año, index=[f'Dia {i}' for i in range(1, 32)])
        datos.to_csv('datos_pluviales.csv')

    return datos

def graficos_de_lluvias():
    datos = obtener_registro_pluviales()
    while True:
        print('=' * 5)
        print('1. Lluvias por mes (Barras).')
        print('2. Grafico de dispersion.')
        print('3. Grafico de torta.')
        print('=' * 5)
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':

            plt.bar()
            plt.show()

        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            return
        else:
            print('Opcion incorrecta.')

def mostrar_registro_pluviales():
    datos = obtener_registro_pluviales()
    mes = input('\nIngrese el mes que desea mostrar: ')
    columna = datos[mes.lower()]
    print(columna)
    input('Presiones enter para continuar...')
