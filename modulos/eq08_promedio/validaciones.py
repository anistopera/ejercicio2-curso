"""
validaciones.py
Módulo compartido de validaciones para el Equipo 08 (Promedio).
Usado por: operaciones_mediana.py, operaciones_promedio.py, operaciones_moda.py
"""

from typing import List, Union

Numero = Union[int, float]


def es_lista_de_numeros(valores) -> bool:
    """
    Verifica que 'valores' sea una lista (no vacía) compuesta solo por
    int o float. No acepta matrices aquí; para eso usar
    es_matriz_de_numeros().
    """
    if not isinstance(valores, list):
        return False
    if len(valores) == 0:
        return False
    return all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in valores)


def es_matriz_de_numeros(valores) -> bool:
    """
    Verifica que 'valores' sea una matriz: una lista de listas,
    donde cada sublista contiene solo int o float, y todas las
    sublistas tienen al menos un elemento.
    """
    if not isinstance(valores, list) or len(valores) == 0:
        return False
    if not all(isinstance(fila, list) for fila in valores):
        return False
    return all(es_lista_de_numeros(fila) for fila in valores)


def aplanar_matriz(matriz: List[List[Numero]]) -> List[Numero]:
    """
    Convierte una matriz (lista de listas) en una sola lista de
    valores, recorriendo fila por fila.
    Ejemplo: [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    """
    return [valor for fila in matriz for valor in fila]


def validar_entrada_numerica(valores) -> List[Numero]:
    """
    Punto de entrada único de validación para las funciones de
    Equipo 08 (mediana, promedio, moda).

    Acepta:
      - Una lista simple de números: [1, 2, 3]
      - Una matriz de números: [[1, 2], [3, 4]]

    Retorna siempre una lista plana de números lista para calcular.
    Lanza ValueError con un mensaje claro si la entrada no es válida.
    """
    if es_lista_de_numeros(valores):
        return valores

    if es_matriz_de_numeros(valores):
        return aplanar_matriz(valores)

    if isinstance(valores, list) and len(valores) == 0:
        raise ValueError("La lista de valores no puede estar vacía.")

    raise ValueError(
        "Entrada inválida: se esperaba una lista o matriz de números "
        "(int o float)."
    )
