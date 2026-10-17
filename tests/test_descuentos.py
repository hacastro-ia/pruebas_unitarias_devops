import pytest
from src.descuentos import (
    aplicar_descuento, calcular_descuento, calcular_precio_final,
    descuento_por_volumen, descuento_cumulativo, descuento_apilado,
)


def test_aplicar_descuento_diez_por_ciento():
    precio, porcentaje = 200, 10

    resultado = aplicar_descuento(precio, porcentaje)

    assert resultado == 180


def test_aplicar_descuento_cero_por_ciento_no_cambia_precio():
    precio, porcentaje = 150, 0

    resultado = aplicar_descuento(precio, porcentaje)

    assert resultado == 150


def test_aplicar_descuento_cien_por_ciento_da_cero():
    precio, porcentaje = 80, 100

    resultado = aplicar_descuento(precio, porcentaje)

    assert resultado == 0


def test_aplicar_descuento_porcentaje_mayor_a_cien_lanza_error():
    precio, porcentaje = 100, 101

    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_precio_negativo_lanza_error():
    precio, porcentaje = -50, 10

    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_calcular_descuento_devuelve_monto():
    precio, porcentaje = 200, 25

    resultado = calcular_descuento(precio, porcentaje)

    assert resultado == 50


def test_calcular_descuento_porcentaje_negativo_lanza_error():
    precio, porcentaje = 100, -5

    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


def test_calcular_precio_final_impuesto_sobre_precio_con_descuento():
    precio, impuesto, descuento = 100, 10, 50

    resultado = calcular_precio_final(precio, impuesto, descuento)

    assert resultado == 55


def test_calcular_precio_final_sin_descuento_ni_impuesto():
    precio, impuesto, descuento = 100, 0, 0

    resultado = calcular_precio_final(precio, impuesto, descuento)

    assert resultado == 100


def test_calcular_precio_final_impuesto_negativo_lanza_error():
    precio, impuesto, descuento = 100, -1, 0

    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


def test_descuento_por_volumen_menos_de_diez_sin_descuento():
    cantidad, precio_unitario = 9, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 90


def test_descuento_por_volumen_diez_unidades_cinco_por_ciento():
    cantidad, precio_unitario = 10, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 95


def test_descuento_por_volumen_cien_unidades_veinte_por_ciento():
    cantidad, precio_unitario = 100, 10

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 800


def test_descuento_por_volumen_cantidad_negativa_lanza_error():
    cantidad, precio_unitario = -1, 10

    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)


def test_descuento_cumulativo_dos_descuentos_sucesivos():
    precio, descuentos = 100, [10, 10]

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == pytest.approx(81)


def test_descuento_cumulativo_lista_vacia_devuelve_precio():
    precio, descuentos = 100, []

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == 100


def test_descuento_cumulativo_descuento_invalido_lanza_error():
    precio, descuentos = 100, [10, 150]

    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)


def test_descuento_apilado_suma_porcentajes():
    precio, descuentos = 100, [10, 20]

    resultado = descuento_apilado(precio, descuentos)

    assert resultado == 70


def test_descuento_apilado_lista_vacia_devuelve_precio():
    precio, descuentos = 100, []

    resultado = descuento_apilado(precio, descuentos)

    assert resultado == 100


def test_descuento_apilado_total_mayor_a_cien_da_cero():
    precio, descuentos = 100, [60, 60]

    resultado = descuento_apilado(precio, descuentos)

    assert resultado == 0
