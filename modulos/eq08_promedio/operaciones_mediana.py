"""
operaciones_mediana.py
HU-801 — Equipo 08 (Promedio)
Subgrupo: Henry, Jhoan, Abby

Implementa la función mediana(valores) sobre listas y/o matrices
de números.
"""

from typing import List, Union
from validaciones import validar_entrada_numerica
import math

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
      - Cantidad IMPAR de elementos -> se retorna el valor central
        tras ordenar.
      - Cantidad PAR de elementos -> se retorna el promedio de los
        dos valores centrales.

    Lanza ValueError si la entrada no es una lista o matriz válida
    de números, o si está vacía.
    """
    # Obtener datos aplanados y validados
    datos: List[Numero] = validar_entrada_numerica(valores)
    
    # Filtrar valores infinitos SOLO si hay otros valores finitos
    valores_finitos = [x for x in datos if not (isinstance(x, float) and (x == float('inf') or x == float('-inf')))]
    
    # Usar valores finitos si existen, sino usar todos
    if valores_finitos:
        datos = valores_finitos
    
    # Ordenar datos
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mitad = n // 2

    if n % 2 == 1:
        # Cantidad impar: el elemento central
        return datos_ordenados[mitad]
    else:
        # Cantidad par: promedio de los dos elementos centrales
        # Usar math.fsum para mejor precisión numérica
        valor_izquierdo = datos_ordenados[mitad - 1]
        valor_derecho = datos_ordenados[mitad]
        
        # Calcular promedio con alta precisión
        return math.fsum([valor_izquierdo, valor_derecho]) / 2