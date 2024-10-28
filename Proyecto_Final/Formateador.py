def formateador(resultados: list, ancho = 20) -> None:

    """
   Esta funcion se encarga de presentar en formato de tabla a traves de la consola los datos que contiene
   resultado.

    Parametros:
        - resultado [list]: Lista de dicionarios que contiene resultados de una consulta SQL.

    Retornos:
        - None: Esta funcion no retorna nada
    """

    if not resultados:
        print('\n' * 50)
        print('La tabla esta vacia...')
        return

    # Creacion e impresion del encambezado de cada tabla.
    print('\n' * 50)
    print('=' * len(resultados[0]) * 31 + '=')
    linea = '|'
    for resultado in resultados[0].keys():
        linea = linea + '{:^30}|'.format(str(resultado))
    print(linea)
    print('=' * len(linea))

    # Insersion de los datos en una tabla e impresion de la misma.
    for registro in resultados:
        linea = '|'
        for atributo in registro.values():
            linea = linea + '{:^30}|'.format(str(atributo))
        print(linea)
        print('-' * len(linea))
    print('')

    continuar = input('\n Presione enter para continuar...')
