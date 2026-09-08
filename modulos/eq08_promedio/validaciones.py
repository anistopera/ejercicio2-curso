"""
validaciones.py
Módulo compartido de validaciones para el Equipo 08 (Promedio).
Usado por: operaciones_mediana.py, operaciones_promedio.py, operaciones_moda.py
"""

from typing import List, Union

# Nota: Se añade 'complex' si el equipo de Promedio Simple lo requiere, 
# pero usualmente promedios y medianas trabajan con int y float.
Numero = Union[int, float, complex]

def es_lista_de_numeros(valores) -> bool:
    """
    Verifica que 'valores' sea una lista (no vacía) compuesta solo por números.
    """
    if not isinstance(valores, list) or len(valores) == 0:
        return False
    # Se unifica la lógica de ambos equipos
    return all(isinstance(x, (int, float, complex)) and not isinstance(x, bool) for x in valores)

def es_matriz_de_numeros(valores) -> bool:
    """
    Verifica que 'valores' sea una matriz: una lista de listas no vacía.
    """
    if not isinstance(valores, list) or len(valores) == 0:
        return False
    if not all(isinstance(fila, list) for fila in valores):
        return False
    return all(es_lista_de_numeros(fila) for fila in valores)

def aplanar_matriz(matriz: List[List[Numero]]) -> List[Numero]:
    """
    Convierte una matriz en una sola lista de valores.
    Ejemplo: [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    """
    return [valor for fila in matriz for valor in fila]

def validar_entrada_numerica(valores) -> List[Numero]:
    """
    Punto de entrada único de validación para las funciones de Equipo 08.
    Retorna siempre una lista plana de números lista para calcular.
    """
    if isinstance(valores, list) and len(valores) == 0:
        raise ValueError("La lista de valores no puede estar vacía.")

    if es_lista_de_numeros(valores):
        return valores

    if es_matriz_de_numeros(valores):
        return aplanar_matriz(valores)

    raise ValueError("Entrada inválida: se esperaba una lista o matriz de números.")

def validar_matrices_mismas_dimensiones(matrices):
    """
    Función aportada por Promedio Simple para validar dimensiones.
    """
    if not matrices:
        raise ValueError("Se espera una lista no vacía de matrices.")
    filas = len(matrices[0])
    columnas = len(matrices[0][0]) if filas > 0 else 0
    for m in matrices:
        if len(m) != filas or any(len(f) != columnas for f in m):
            return False
    return True