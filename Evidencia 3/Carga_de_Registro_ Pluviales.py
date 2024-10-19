import random
import pandas as pd
import calendar
import os

# Sección 1: Funciones de utilidad
# Esta sección contiene funciones auxiliares para manejar fechas y cálculos relacionados con el tiempo

def is_leap_year(year):
    """
    Determina si un año es bisiesto.
    
    Args:
    year (int): El año a verificar.
    
    Returns:
    bool: True si es bisiesto, False si no.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """
    Calcula el número de días en un mes específico.
    
    Args:
    year (int): El año.
    month (int): El mes (1-12).
    
    Returns:
    int: El número de días en el mes.
    """
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# Sección 2: Generación y manipulación de datos
# Esta sección contiene funciones para generar, cargar y manipular los datos de lluvia

def generate_rainfall_data(year):
    """
    Genera datos de lluvia aleatorios para un año completo.
    
    Args:
    year (int): El año para el que se generan los datos.
    
    Returns:
    list: Una lista de listas con los datos de lluvia para cada mes.
    """
    rainfall_data = []
    for month in range(1, 13):
        days = days_in_month(year, month)
        month_data = [round(random.uniform(0, 50), 1) for _ in range(days)]
        rainfall_data.append(month_data)
    return rainfall_data

def create_dataframe(rainfall_data, year):
    """
    Crea un DataFrame de pandas a partir de los datos de lluvia generados.
    
    Args:
    rainfall_data (list): Lista de listas con los datos de lluvia.
    year (int): El año de los datos.
    
    Returns:
    pandas.DataFrame: DataFrame con los datos de lluvia organizados.
    """
    max_days = max(len(month) for month in rainfall_data)
    df = pd.DataFrame(index=range(1, max_days + 1))
    
    for month, data in enumerate(rainfall_data, 1):
        month_name = calendar.month_abbr[month]
        df[month_name] = pd.Series(data, index=range(1, len(data) + 1))
    
    df.index.name = 'Day'
    return df

def load_or_generate_data(year):
    """
    Carga datos existentes de un archivo CSV o genera nuevos datos si el archivo no existe.
    
    Args:
    year (int): El año para el cual se cargan o generan los datos.
    
    Returns:
    pandas.DataFrame: DataFrame con los datos de lluvia.
    """
    filename = f"registroPluvial{year}.csv"
    if os.path.exists(filename):
        print(f"Cargando datos existentes de {filename}")
        df = pd.read_csv(filename, index_col='Day')
    else:
        print(f"Generando nuevos datos de lluvia para {year}")
        rainfall_data = generate_rainfall_data(year)
        df = create_dataframe(rainfall_data, year)
        df.to_csv(filename)
        print(f"Datos guardados en {filename}")
    return df

# Sección 3: Visualización de datos
# Esta sección contiene funciones para mostrar los datos de lluvia de diferentes maneras

def display_monthly_data(df, month, year):
    """
    Muestra los datos de lluvia para un mes específico.
    
    Args:
    df (pandas.DataFrame): DataFrame con los datos de lluvia.
    month (int): El mes a mostrar (1-12).
    year (int): El año de los datos.
    """
    month_name = calendar.month_name[month]
    month_abbr = calendar.month_abbr[month]
    print(f"\nDatos de lluvia para {month_name} {year}:")
    days = days_in_month(year, month)
    month_data = df[month_abbr].head(days)
    print(month_data.to_string())
    print(f"\nTotal de lluvia en {month_name}: {month_data.sum():.1f} mm")
    print(f"Promedio diario de lluvia: {month_data.mean():.1f} mm")

def display_annual_summary(df, year):
    """
    Muestra un resumen anual de los datos de lluvia.
    
    Args:
    df (pandas.DataFrame): DataFrame con los datos de lluvia.
    year (int): El año de los datos.
    """
    print(f"\nResumen anual de lluvia para {year}:")
    annual_total = df.sum().sum()
    print(f"Total anual de lluvia: {annual_total:.1f} mm")
    monthly_totals = df.sum()
    print("\nTotales mensuales:")
    for month, total in monthly_totals.items():
        print(f"{month}: {total:.1f} mm")
    print(f"\nMes más lluvioso: {monthly_totals.idxmax()} con {monthly_totals.max():.1f} mm")
    print(f"Mes menos lluvioso: {monthly_totals.idxmin()} con {monthly_totals.min():.1f} mm")

# Sección 4: Función principal y manejo de la interfaz de usuario
# Esta sección contiene la función principal que maneja la interacción con el usuario

def main():
    """
    Función principal que maneja la interacción con el usuario y coordina las operaciones del programa.
    """
    location = "Córdoba, Argentina"
    year = int(input("Ingrese el año para los datos de lluvia (ej. 2023): "))
    
    df = load_or_generate_data(year)
    
    print(f"\nDatos de lluvia para {location} en {year} han sido cargados/generados.")
    
    while True:
        print("\nOpciones:")
        print("1. Ver datos de un mes específico")
        print("2. Ver resumen anual")
        print("3. Exportar datos a CSV")
        print("0. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            month = int(input("Ingrese un número de mes (1-12): "))
            if 1 <= month <= 12:
                display_monthly_data(df, month, year)
            else:
                print("Mes inválido. Por favor ingrese un número entre 1 y 12.")
        elif choice == '2':
            display_annual_summary(df, year)
        elif choice == '3':
            filename = f"registroPluvial{year}_exportado.csv"
            df.to_csv(filename)
            print(f"Datos exportados a {filename}")
        elif choice == '0':
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")

# Sección 5: Punto de entrada del programa
if __name__ == "__main__":
    main()
