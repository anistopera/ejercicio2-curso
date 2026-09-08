"""
operaciones_mediana.py
HU-801 — Equipo 08 (Promedio)
Subgrupo: Henry, Jhoan, Abby

Implementa la función mediana(valores) sobre listas y/o matrices
de números.
"""

from typing import List, Union
from .validaciones import validar_entrada_numerica

Numero = Union[int, float]


def mediana(valores) -> Numero:
    """
    Calcula la mediana de una lista o matriz de números.

    Reglas:
      - Si la entrada es una lista simple, se calcula la mediana
        directamente sobre sus elementos.
      - Si la entrada es una matriz (lista de listas), se aplanan
        todos sus valores en una sola secuencia y se calcula la
        mediana sobre el conjunto combinado.
        (Asunción documentada: el manual no especifica si la mediana
        de una matriz debe ser por fila o global; aquí se usa la
        mediana global. Confirmar con el equipo/profesor si se
        requiere mediana por fila.)
      - Cantidad IMPAR de elementos -> se retorna el valor central
        tras ordenar.
      - Cantidad PAR de elementos -> se retorna el promedio de los
        dos valores centrales.

    Lanza ValueError si la entrada no es una lista o matriz válida
    de números, o si está vacía.

    Ejemplos:
        >>> mediana([3, 1, 2])
        2
        >>> mediana([4, 1, 2, 3])
        2.5
        >>> mediana([[1, 2], [3, 4, 5]])
        3
    """
    datos: List[Numero] = validar_entrada_numerica(valores)

    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mitad = n // 2

    if n % 2 == 1:
        # Cantidad impar: el elemento central.
        # Ejemplo: [1, 2, 3] -> n=3, mitad=1 -> datos_ordenados[1] = 2
        return datos_ordenados[mitad]
    else:
        # Cantidad par: promedio de los dos elementos centrales.
        # Ejemplo: [1, 2, 3, 4] -> n=4, mitad=2
        # -> promedio(datos_ordenados[1], datos_ordenados[2]) = (2+3)/2 = 2.5
        valor_izquierdo = datos_ordenados[mitad - 1]
        valor_derecho = datos_ordenados[mitad]
        return (valor_izquierdo + valor_derecho) / 2
