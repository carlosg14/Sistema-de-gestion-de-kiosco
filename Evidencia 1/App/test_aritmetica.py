from aritmetica import *


def suma_test() -> None:

    # Probamos si se realiza correctamente la suma.
    a, b = 1, 2
    assert sumar(a, b) == 3
    a, b = -4, -3
    assert sumar(a, b) == -7
    a, b = 3, -2
    assert sumar(a, b) == 1


def resta_test():

    # Probamos la funcion restar
    a, b = 1, 2
    assert restar(a, b) == -1
    a, b = 4, 3
    assert restar(a, b) == 1
    a, b = 3, -2
    assert restar(a, b) == 5


def multiplicar_test():

    # Probamos la funcion multiplicar
    a, b = 1, 2
    assert multiplicar(a, b) == 2
    a, b = -4, -1
    assert multiplicar(a, b) == 4
    a, b = 3, -2
    assert multiplicar(a, b) == -6


def dividir_test():

    a, b = 1, 2
    assert dividir(a, b) == 0.5
    a, b = -4, -3
    assert dividir(a, b) == 1.33
    a, b = 3, -2
    assert dividir(a, b) == -1.5

def suma_n_test():

    a, b = 1, 2
    assert sumar_n(a, b) == 3
    a, b = -4, -3
    assert sumar_n(a, b) == -7
    a, b = 3, -2
    assert sumar_n(a, b) == 1

def promedio_n_test():
    a, b = 1, 2
    assert promedio_n(a, b) == 1.5
    a, b = -4, -3
    assert promedio_n(a, b) == -3.5
    a, b = 3, -2
    assert promedio_n(a, b) == 0.5

if __name__ == '__main__':
    suma_test()
    resta_test()
    multiplicar_test()
    dividir_test()
    suma_n_test()
    promedio_n_test()
