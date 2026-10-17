import pytest
from unittest.mock import patch, mock_open
from src.csv_parser import (
    parse_csv_line, leer_csv_como_lista, csv_a_diccionarios,
    validar_csv, extraer_columna, filtrar_por_columna,
    contar_filas, contar_columnas,
)


def test_parse_csv_line_vacia_devuelve_lista_vacia():
    linea = ""

    resultado = parse_csv_line(linea)

    assert resultado == []


def test_parse_csv_line_campos_simples():
    linea = "a,b,c"

    resultado = parse_csv_line(linea)

    assert resultado == ["a", "b", "c"]


def test_parse_csv_line_comillas_con_coma_interna():
    linea = '"Perez, Juan",30'

    resultado = parse_csv_line(linea)

    assert resultado == ["Perez, Juan", "30"]


def test_parse_csv_line_comillas_escapadas():
    linea = '"dijo ""hola""",1'

    resultado = parse_csv_line(linea)

    assert resultado == ['dijo "hola"', "1"]


def test_leer_csv_como_lista_contenido_vacio():
    contenido = ""

    resultado = leer_csv_como_lista(contenido)

    assert resultado == []


def test_leer_csv_como_lista_dos_filas():
    contenido = "a,b\n1,2"

    resultado = leer_csv_como_lista(contenido)

    assert resultado == [["a", "b"], ["1", "2"]]


def test_leer_csv_como_lista_con_parse_simulado():
    contenido = "linea1\nlinea2"

    with patch("src.csv_parser.parse_csv_line", return_value=["x"]) as parse_falso:
        resultado = leer_csv_como_lista(contenido)

    assert resultado == [["x"], ["x"]]
    assert parse_falso.call_count == 2


def test_leer_csv_desde_archivo_simulado_sin_tocar_disco():
    datos_falsos = "nombre,edad\nAna,30\n"

    with patch("builtins.open", mock_open(read_data=datos_falsos)) as abrir_falso:
        with open("archivo_inexistente.csv") as archivo:
            contenido = archivo.read()
        resultado = leer_csv_como_lista(contenido)

    abrir_falso.assert_called_once_with("archivo_inexistente.csv")
    assert resultado == [["nombre", "edad"], ["Ana", "30"]]


def test_csv_a_diccionarios_con_cabecera():
    contenido = "nombre,edad\nAna,30\nLuis,25"

    resultado = csv_a_diccionarios(contenido)

    assert resultado == [
        {"nombre": "Ana", "edad": "30"},
        {"nombre": "Luis", "edad": "25"},
    ]


def test_csv_a_diccionarios_fila_con_menos_columnas():
    contenido = "a,b,c\n1,2"

    resultado = csv_a_diccionarios(contenido)

    assert resultado == [{"a": "1", "b": "2", "c": ""}]


def test_csv_a_diccionarios_contenido_vacio():
    contenido = ""

    resultado = csv_a_diccionarios(contenido)

    assert resultado == []


def test_csv_a_diccionarios_solo_cabecera_devuelve_lista_vacia():
    contenido = "a,b"

    resultado = csv_a_diccionarios(contenido)

    assert resultado == []


def test_csv_a_diccionarios_sin_cabecera_devuelve_lista_vacia():
    contenido = "1,2\n3,4"

    resultado = csv_a_diccionarios(contenido, tiene_cabecera=False)

    assert resultado == []


def test_validar_csv_formato_correcto():
    contenido = "a,b\n1,2\n3,4"

    resultado = validar_csv(contenido)

    assert resultado is True


def test_validar_csv_filas_con_distinto_numero_de_comas():
    contenido = "a,b\n1,2,3"

    resultado = validar_csv(contenido)

    assert resultado is False


def test_validar_csv_contenido_vacio():
    contenido = ""

    resultado = validar_csv(contenido)

    assert resultado is False


def test_extraer_columna_existente():
    contenido = "a,b\n1,2"

    resultado = extraer_columna(contenido, 1)

    assert resultado == ["b", "2"]


def test_extraer_columna_fuera_de_rango_devuelve_vacios():
    contenido = "a,b\n1,2"

    resultado = extraer_columna(contenido, 5)

    assert resultado == ["", ""]


def test_extraer_columna_contenido_vacio():
    contenido = ""

    resultado = extraer_columna(contenido, 0)

    assert resultado == []


def test_filtrar_por_columna_con_coincidencias():
    contenido = "a,x\nb,y\nc,x"

    resultado = filtrar_por_columna(contenido, 1, "x")

    assert resultado == [["a", "x"], ["c", "x"]]


def test_filtrar_por_columna_contenido_vacio():
    contenido = ""

    resultado = filtrar_por_columna(contenido, 0, "x")

    assert resultado == []


def test_contar_filas_tres_filas():
    contenido = "a,b\n1,2\n3,4"

    resultado = contar_filas(contenido)

    assert resultado == 3


def test_contar_filas_contenido_vacio():
    contenido = ""

    resultado = contar_filas(contenido)

    assert resultado == 0


def test_contar_columnas_tres_columnas():
    contenido = "a,b,c\n1,2,3"

    resultado = contar_columnas(contenido)

    assert resultado == 3


def test_contar_columnas_contenido_vacio():
    contenido = ""

    resultado = contar_columnas(contenido)

    assert resultado == 0
