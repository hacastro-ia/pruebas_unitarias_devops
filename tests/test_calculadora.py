import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, promedio, maximo, minimo,
    calcular_area_rectangulo, calcular_perimetro_rectangulo,
)


def test_sumar_positivos():
    a, b = 7, 5

    resultado = sumar(a, b)

    assert resultado == 12


def test_restar_resultado_negativo():
    a, b = 3, 10

    resultado = restar(a, b)

    assert resultado == -7


def test_multiplicar_por_cero():
    a, b = 9, 0

    resultado = multiplicar(a, b)

    assert resultado == 0


def test_dividir_por_cero_lanza_error():
    a, b = 10, 0

    with pytest.raises(ValueError):
        dividir(a, b)


def test_potencia_exponente_cero():
    base, exponente = 5, 0

    resultado = potencia(base, exponente)

    assert resultado == 1


def test_raiz_cuadrada_numero_positivo():
    numero = 16

    resultado = raiz_cuadrada(numero)

    assert resultado == 4


def test_raiz_cuadrada_negativo_lanza_error():
    numero = -4

    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


def test_minimo_con_todos_positivos():
    lista = [5, 3, 8]

    resultado = minimo(lista)

    assert resultado == 3


def test_minimo_lista_vacia_lanza_error():
    lista = []

    with pytest.raises(ValueError):
        minimo(lista)


def test_promedio_lista_simple():
    lista = [2, 4, 6]

    resultado = promedio(lista)

    assert resultado == 4
