import pytest
from src.conversor import (
    celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin,
    kelvin_a_celsius, metros_a_kilometros, kilometros_a_metros,
    libras_a_kilogramos, kilogramos_a_libras, galones_a_litros,
    litros_a_galones, millas_a_kilometros, kilometros_a_millas,
    pies_a_metros, metros_a_pies, onzas_a_gramos, gramos_a_onzas,
)


def test_celsius_a_fahrenheit_punto_de_congelacion():
    celsius = 0

    resultado = celsius_a_fahrenheit(celsius)

    assert resultado == 32


def test_celsius_a_fahrenheit_punto_de_ebullicion():
    celsius = 100

    resultado = celsius_a_fahrenheit(celsius)

    assert resultado == 212


def test_fahrenheit_a_celsius_punto_de_congelacion():
    fahrenheit = 32

    resultado = fahrenheit_a_celsius(fahrenheit)

    assert resultado == 0


def test_celsius_a_kelvin_cero_celsius():
    celsius = 0

    resultado = celsius_a_kelvin(celsius)

    assert resultado == pytest.approx(273.15)


def test_kelvin_a_celsius_valor_valido():
    kelvin = 273.15

    resultado = kelvin_a_celsius(kelvin)

    assert resultado == pytest.approx(0)


def test_kelvin_a_celsius_cero_absoluto():
    kelvin = 0

    resultado = kelvin_a_celsius(kelvin)

    assert resultado == pytest.approx(-273.15)


def test_kelvin_a_celsius_negativo_lanza_error():
    kelvin = -10

    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)


def test_metros_a_kilometros_mil_metros():
    metros = 1000

    resultado = metros_a_kilometros(metros)

    assert resultado == 1


def test_metros_a_kilometros_negativo_lanza_error():
    metros = -1

    with pytest.raises(ValueError):
        metros_a_kilometros(metros)


def test_kilometros_a_metros_dos_kilometros():
    kilometros = 2

    resultado = kilometros_a_metros(kilometros)

    assert resultado == 2000


def test_kilometros_a_metros_negativo_lanza_error():
    kilometros = -2

    with pytest.raises(ValueError):
        kilometros_a_metros(kilometros)


def test_libras_a_kilogramos_diez_libras():
    libras = 10

    resultado = libras_a_kilogramos(libras)

    assert resultado == pytest.approx(4.53592)


def test_libras_a_kilogramos_negativo_lanza_error():
    libras = -1

    with pytest.raises(ValueError):
        libras_a_kilogramos(libras)


def test_kilogramos_a_libras_un_kilogramo():
    kilogramos = 1

    resultado = kilogramos_a_libras(kilogramos)

    assert resultado == pytest.approx(2.20462, rel=1e-4)


def test_kilogramos_a_libras_negativo_lanza_error():
    kilogramos = -1

    with pytest.raises(ValueError):
        kilogramos_a_libras(kilogramos)


def test_galones_a_litros_un_galon():
    galones = 1

    resultado = galones_a_litros(galones)

    assert resultado == pytest.approx(3.78541)


def test_galones_a_litros_negativo_lanza_error():
    galones = -1

    with pytest.raises(ValueError):
        galones_a_litros(galones)


def test_litros_a_galones_un_galon_en_litros():
    litros = 3.78541

    resultado = litros_a_galones(litros)

    assert resultado == pytest.approx(1)


def test_litros_a_galones_negativo_lanza_error():
    litros = -1

    with pytest.raises(ValueError):
        litros_a_galones(litros)


def test_millas_a_kilometros_una_milla():
    millas = 1

    resultado = millas_a_kilometros(millas)

    assert resultado == pytest.approx(1.60934)


def test_millas_a_kilometros_negativo_lanza_error():
    millas = -1

    with pytest.raises(ValueError):
        millas_a_kilometros(millas)


def test_kilometros_a_millas_una_milla_en_kilometros():
    kilometros = 1.60934

    resultado = kilometros_a_millas(kilometros)

    assert resultado == pytest.approx(1)


def test_kilometros_a_millas_negativo_lanza_error():
    kilometros = -1

    with pytest.raises(ValueError):
        kilometros_a_millas(kilometros)


def test_pies_a_metros_diez_pies():
    pies = 10

    resultado = pies_a_metros(pies)

    assert resultado == pytest.approx(3.048)


def test_pies_a_metros_negativo_lanza_error():
    pies = -1

    with pytest.raises(ValueError):
        pies_a_metros(pies)


def test_metros_a_pies_un_pie_en_metros():
    metros = 0.3048

    resultado = metros_a_pies(metros)

    assert resultado == pytest.approx(1)


def test_metros_a_pies_negativo_lanza_error():
    metros = -1

    with pytest.raises(ValueError):
        metros_a_pies(metros)


def test_onzas_a_gramos_una_onza():
    onzas = 1

    resultado = onzas_a_gramos(onzas)

    assert resultado == pytest.approx(28.3495)


def test_onzas_a_gramos_negativo_lanza_error():
    onzas = -1

    with pytest.raises(ValueError):
        onzas_a_gramos(onzas)


def test_gramos_a_onzas_una_onza_en_gramos():
    gramos = 28.3495

    resultado = gramos_a_onzas(gramos)

    assert resultado == pytest.approx(1)


def test_gramos_a_onzas_negativo_lanza_error():
    gramos = -1

    with pytest.raises(ValueError):
        gramos_a_onzas(gramos)
