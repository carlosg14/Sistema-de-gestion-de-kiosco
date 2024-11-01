# Proyecto Final

En este proyecto se implementa un programa que ofrece un amplio rango de funcionalidades, que van desde un CRUD de usuarios almacenados en archivos binarios hasta la utilización de una base de datos en MySql.

## Requisitos

- [Python 3.x 🐍](https://www.python.org/downloads/)
- [MySql 8.0 🐬](https://dev.mysql.com/downloads/installer/)
- [mysql-connector-python🔌](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)
- [Pandas 🐼](https://pandas.pydata.org/docs/getting_started/install.html)
- [Numpy 🔢](https://numpy.org/install/)
- [Matplotlib 📊](https://matplotlib.org/stable/install/index.html)

## Módulos del programa

* **Carga de registros pluviales:** Las funciones de las que se ocupa este módulo son: Generar un archivo csv con registros de precipitaciones de un año, generar gráficos relacionados con precipitaciones y calcular medidas estadísticas como la media, promedio, etc.
* **Consultas:** En este módulo se encuentran las consultas que se realizarán a la base de datos.
* **Formateador:** Este módulo le da formato de tabla a los datos que se le pasan como parámetro. Estos datos son los que se obtienen luego de las consultas a la BD.
* **Algorimos_ordenamiento:** En este modulo se encuentran los algoritmos de ordenamiento y busqueda que son utilizados por otros modulos del programa.
* **Clase_acceso:** En este modulo se encuentran todo el codigo relacionado con los accesos.
* **Clase_usuario**: En este modulo se encuentran todo el codigo relacionado con los usuarios, como por ejemplo el CRUD de usuarios.
* **config**: En este archivo se guardan datos para configurar el programa tales como las credenciales para acceder a la BD.
* **Gestion_de_archivos**: En este modulo se encuentran las funciones encargadas de leer y escribir archivos binarios y de texto.
* **Main**: Desde este archivo se accede al programa. El mismo presenta al usuario un menu atraves de la linea de comandos.
*  **Conexion_BD.py**: Este módulo se encarga de abrir una conexion con la bd y realizar la consulta que se le pase por parametros.Luego de esto se cierra la conexion con la                        BD.
## Mapa de aplicacion

![](./Python.png)
