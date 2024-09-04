def sumar(a: float, b: float):
    return round(a + b, 2)

def restar(a: float, b: float):
    return round(a - b, 2)

def dividir(a: float, b: float):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        b += 1
        return round(a / b, 2)

def multiplicar(a: float, b: float):
    return round(a * b, 2)

def sumar_n(*numeros: float):
    suma = 0
    for numero in numeros:
        suma = sumar(suma, numero)
    return round(suma, 2)


def promedio_n(*numeros: float):
    suma = sumar_n(*numeros)
    return round(dividir(suma, len(numeros)), 2)



