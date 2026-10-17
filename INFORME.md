# Informe: Analisis y Mejora de Pruebas Unitarias

## 1. Datos

- **Nombre:** Hamilton Castro Marin
- **Grupo:** 1
- **Fecha:** 17 de octubre de 2026
- **Curso:** Introduccion a DevOps, Universidad Nacional de Colombia, Sede Manizales
- **Repositorio:** fork de cesarpalacios/pruebas_unitarias_devops

## 2. Analisis por modulo

### calculadora.py

Reune operaciones matematicas basicas (suma, resta, multiplicacion, division, potencia, raiz cuadrada), estadisticas sobre listas (promedio, maximo, minimo) y calculos de area y perimetro de un rectangulo.

Casos probados y por que:
- Operaciones basicas con valores positivos, negativos y cero, para confirmar el resultado aritmetico y el comportamiento con el elemento neutro.
- Division por cero, porque la funcion debe lanzar `ValueError`.
- Raiz cuadrada de un numero positivo y de un negativo, ya que el negativo es el caso donde la funcion podia fallar.
- Promedio, maximo y minimo con listas simples, listas con negativos y listas vacias. El minimo con una lista de solo positivos revela el bug de inicializacion.
- Area y perimetro con valores validos y con valores negativos, para verificar las validaciones de entrada.

### descuentos.py

Calcula precios con descuentos e impuestos: descuento simple, monto del descuento, precio final con impuesto, descuento por volumen, descuentos sucesivos (acumulativos) y descuentos sumados (apilados).

Casos probados y por que:
- Porcentajes en los limites (0 %, 100 %) y fuera de rango (101 %, negativos), porque son los valores donde las validaciones pueden fallar.
- Precios negativos en todas las funciones, para ejercitar cada rama de error.
- Precio final combinando impuesto y descuento, que expone el error en el orden del calculo.
- Descuento por volumen en cada tramo (menos de 10, 10, 20, 50 y 100 unidades), para confirmar los umbrales.
- Descuentos acumulativos y apilados con listas vacias, listas normales y listas cuya suma supera 100 %.

### conversor.py

Convierte unidades de temperatura (Celsius, Fahrenheit, Kelvin), longitud (metros, kilometros, millas, pies), masa (libras, kilogramos, onzas, gramos) y volumen (galones, litros).

Casos probados y por que:
- Valores de referencia conocidos (0 grados C = 32 grados F, 100 grados C = 212 grados F, 0 grados C = 273.15 K, una milla = 1.60934 km), para comparar contra resultados verificables.
- Conversion de ida y vuelta con el valor equivalente a una unidad, para detectar formulas que multiplican en lugar de dividir.
- Entradas negativas en cada funcion que valida, porque cada una debe lanzar `ValueError`.
- Cero absoluto y Kelvin negativo, el caso limite fisico de la escala.
- Comparaciones con `pytest.approx`, porque los factores de conversion producen numeros decimales.

## 3. Tabla de bugs

| # | Funcion | Entrada | Resultado erroneo | Resultado esperado | Correccion |
|---|---------|---------|-------------------|--------------------|------------|
| 1 | `calculadora.raiz_cuadrada` | `-4` | Devuelve un numero complejo sin lanzar error | `ValueError` | Se valido `numero < 0` antes de calcular |
| 2 | `calculadora.minimo` | `[5, 3, 8]` | `0` | `3` | Se inicializo `min_val = lista[0]` en lugar de `0` |
| 3 | `descuentos.calcular_precio_final` | precio 100, impuesto 10, descuento 50 | `60` | `55` | El impuesto se calcula sobre `precio_con_descuento` y no sobre el precio original |
| 4 | `descuentos.descuento_apilado` | `100, [60, 60]` | Lanza un error de validacion generico (el total es 120) | `0` (descuento limitado al 100 %) | Se limito el total con `min(total_descuento, 100)` |
| 5 | `conversor.kelvin_a_celsius` | `-10` | `-283.15` | `ValueError` | Se valido `kelvin < 0` |
| 6 | `conversor.kilometros_a_millas` | `1.60934` | `2.59` aprox. | `1.0` | Se cambio la multiplicacion por division |

Cada correccion tiene su propio commit con prefijo `fix:`.

## 4. Cobertura

Comando utilizado:

    pytest tests/ -v --cov=src --cov-report=term-missing

Salida del reporte:

<pre>
---------- coverage: platform linux, python 3.13.5-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/__init__.py                0      0   100%
src/autenticacion.py          42     42     0%   6-77
src/calculadora.py            44      1    98%   22
src/conversor.py              58      0   100%
src/csv_parser.py             76     76     0%   6-127
src/descuentos.py             59      0   100%
src/fibonacci.py              42     42     0%   6-73
src/manipulador_texto.py      93     93     0%   6-156
src/procesador_texto.py       49     49     0%   6-84
src/utils.py                  53     53     0%   6-92
src/validador.py              64     64     0%   6-117
--------------------------------------------------------
TOTAL                        580    420    28%
</pre>

Lectura de resultados:

Los tres modulos trabajados (`calculadora.py`, `descuentos.py` y `conversor.py`) superan la meta del 85 % de cobertura: `calculadora.py` llega al 98 %, y `descuentos.py` y `conversor.py` al 100 %. Los demas modulos de `src/` aparecen en 0 % porque no formaron parte del taller, por lo que el total general (cercano al 28 %) no refleja el trabajo realizado: la meta se evalua solo sobre los modulos trabajados.

En `calculadora.py` solo queda sin cubrir la linea 22, el `return` de `dividir`, porque esa funcion solo se probo con el caso de error (division por cero) y no con una division valida. Es una limitacion conocida que se dejo documentada.

## 5. Reflexion final

**Que NO mide la cobertura?**

La cobertura indica que lineas se ejecutaron durante las pruebas, pero no si las pruebas verifican algo util. Una linea puede ejecutarse sin que ningun `assert` compruebe su resultado, y aun asi contarse como cubierta. Tampoco mide los casos de entrada que no se me ocurrieron: un modulo con 100 % de cobertura puede seguir teniendo errores con datos que nunca se probaron. Ademas, no evalua la integracion entre modulos, el rendimiento ni si el comportamiento esperado definido en las pruebas es el correcto desde el punto de vista del problema. El caso de `dividir` lo muestra: el 98 % de `calculadora.py` oculta que la division normal nunca se probo.

**Que aprendi?**

Aprendi que una prueba en rojo es algo que nos da informacion y no un fracaso: los seis bugs aparecieron porque escribi pruebas para entradas limite como negativos, ceros y listas con valores distintos de cero. Tambien aprendi que la cobertura es una guia para saber que falta probar. En lo practico, aprendi el flujo de trabajo: hacer un fork, autenticarse con un token, escribir pruebas, corregir con commits pequenos y claros, medir y documentar todo dentro del mismo repositorio, no solo eso, tambien el manejo de los comandos, saber que hace cada uno y como hacerlo, tener una estructura y un orden para que no se vuelva un enredo hacer todas las pruebas, si bien la ia me ayudo en partes que me veia perdido tambien sirvio para entender como hacer ciertas cosas y que debo hacer en determinados casos

## 6. Extras

### Extra 1: pruebas de csv_parser.py con mocking

Las funciones de csv_parser.py reciben el contenido como texto, por lo que el modulo no abre archivos. Aun asi se uso unittest.mock de dos formas: `patch` sobre `parse_csv_line` para probar `leer_csv_como_lista` de forma aislada, y `mock_open` para simular un archivo y pasar su contenido al parser, sin tocar el disco.

### Extra 2: bugs corregidos en un modulo no obligatorio

| # | Funcion | Entrada | Resultado erroneo | Resultado esperado | Correccion |
|---|---------|---------|-------------------|--------------------|------------|
| 7 | `csv_parser.parse_csv_line` | `"Perez, Juan",30` | `['"Perez', ' Juan"', '30']` | `['Perez, Juan', '30']` | Se reemplazo `split(',')` por `csv.reader` |
| 8 | `csv_parser.csv_a_diccionarios` | cabecera `a,b,c` y fila `1,2` | `{'a': '1', 'b': '2'}` sin la clave `c` | `{'a': '1', 'b': '2', 'c': ''}` | Se recorren las cabeceras y se completa con cadena vacia |
