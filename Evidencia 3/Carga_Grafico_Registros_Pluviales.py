import pandas as pd
import numpy as np
import calendar
import os
import matplotlib.pyplot as plt

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
    return calendar.monthrange(year, month)[1]

# Sección 2: Generación y manipulación de datos
# Esta sección contiene funciones para generar, cargar y manipular los datos de lluvia

def generate_rainfall_data(year):
    """
    Genera datos de lluvia aleatorios para un año completo utilizando un DataFrame de Pandas.
    
    Args:
    year (int): El año para el que se generan los datos.
    
    Returns:
    pandas.DataFrame: DataFrame con los datos de lluvia organizados por mes y día.
    """
    months = calendar.month_abbr[1:]
    data = {month: np.random.uniform(0, 50, days_in_month(year, i+1)).round(1) 
            for i, month in enumerate(months)}
    
    df = pd.DataFrame(data)
    df.index = range(1, 32)  # Establecer índice de 1 a 31
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
        df = generate_rainfall_data(year)
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

# Sección 4: Visualización gráfica con matplotlib
# Esta sección contiene funciones para crear gráficos de los datos de lluvia

def plot_annual_rainfall(df, year):
    """
    Crea un gráfico de barras de las lluvias anuales.
    
    Args:
    df (pandas.DataFrame): DataFrame con los datos de lluvia.
    year (int): El año de los datos.
    """
    monthly_totals = df.sum()
    plt.figure(figsize=(12, 6))
    plt.bar(monthly_totals.index, monthly_totals.values)
    plt.title(f'Lluvia Anual en Córdoba, Argentina - {year}')
    plt.xlabel('Mes')
    plt.ylabel('Lluvia Total (mm)')
    plt.savefig(f'lluvia_anual_{year}.png')
    plt.close()
    print(f"Gráfico de barras guardado como 'lluvia_anual_{year}.png'")

def plot_rainfall_heatmap(df, year):
    """
    Crea un gráfico de dispersión (heatmap) de la lluvia diaria.
    
    Args:
    df (pandas.DataFrame): DataFrame con los datos de lluvia.
    year (int): El año de los datos.
    """
    plt.figure(figsize=(12, 8))
    for month in range(1, 13):
        month_abbr = calendar.month_abbr[month]
        month_data = df[month_abbr]
        days = days_in_month(year, month)
        plt.scatter([month] * days, range(1, days + 1), c=month_data[:days], cmap='Blues', s=50)
    
    plt.colorbar(label='Lluvia (mm)')
    plt.title(f'Distribución de Lluvia Diaria en Córdoba, Argentina - {year}')
    plt.xlabel('Mes')
    plt.ylabel('Día')
    plt.yticks(range(1, 32, 5))
    plt.xticks(range(1, 13), calendar.month_abbr[1:])
    plt.savefig(f'distribucion_lluvia_{year}.png')
    plt.close()
    print(f"Gráfico de dispersión guardado como 'distribucion_lluvia_{year}.png'")

def plot_monthly_rainfall_pie(df, year):
    """
    Crea un gráfico circular de la distribución mensual de lluvia.
    
    Args:
    df (pandas.DataFrame): DataFrame con los datos de lluvia.
    year (int): El año de los datos.
    """
    monthly_totals = df.sum()
    plt.figure(figsize=(10, 10))
    plt.pie(monthly_totals.values, labels=monthly_totals.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribución Mensual de Lluvia en Córdoba, Argentina - {year}')
    plt.axis('equal')
    plt.savefig(f'distribucion_mensual_{year}.png')
    plt.close()
    print(f"Gráfico circular guardado como 'distribucion_mensual_{year}.png'")

# Sección 5: Función principal y manejo de la interfaz de usuario
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
        print("4. Generar gráfico de barras anual")
        print("5. Generar gráfico de dispersión diaria")
        print("6. Generar gráfico circular mensual")
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
        elif choice == '4':
            plot_annual_rainfall(df, year)
        elif choice == '5':
            plot_rainfall_heatmap(df, year)
        elif choice == '6':
            plot_monthly_rainfall_pie(df, year)
        elif choice == '0':
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")

# Sección 6: Punto de entrada del programa
if __name__ == "__main__":
    main()
