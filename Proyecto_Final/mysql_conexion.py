import mysql.connector
import config


def conexion(query: str, datos: tuple = None, tipo: int = 1) -> list[dict] | int:
    """
        Desde esta funcion se realiza la conexion a la base de datos y se ejecuta
        el comando sql que se recibe como parametro.

        Parametros:

            comando_sql[String]: Cadena de texto que contiene un comando sql, tal como: 'SELECT * FROM table_1'.
            datos[Dict]: Este diccionario contiene los datos necesarios para ejecutar el comando sql.
            tipo[Int]: Nos informa el tipo de comando sql. Puede tomar los siguientes valores:
                       1 -> Consulta, 2 -> Insercion, 3 -> Actualizacion, 4 -> Eliminacion.

        Retornos:

            Lo que se retorne depende del tipo de secuencia sql que se ejecuto.
            Si se ejecuto una consulta entonces se retornan los registros correspondientes en forma de una lista
            de tuplas o diccionarios. Para los demas casos (Insercion, Actualizacion y Eliminacion) se devuelve la confirmacion
            de la operacion o el id del ultimo registro insertado o borrado.
        """
    # Se inicia la conexion con la BD.
    conexion = mysql.connector.connect(**config.config)

    # Se ejecuta el comando sql.
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(query, datos)

    # En base al tipo de operacion se retorna lo que corresponde.
    if tipo == 1:
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado
    else:
        conexion.commit()
        row_id = cursor.lastrowid
        cursor.close()
        conexion.close()

    return row_id