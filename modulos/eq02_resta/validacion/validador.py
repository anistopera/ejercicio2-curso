"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargados: [Rodrigo Mamani Rocha, Santiago Piscoya Bellido]
"""
import math

def validar_entero(valor) -> bool:
    """Valida que el valor sea especificamente un entero (para resta_enteros)."""
    return isinstance(valor, int) and not isinstance(valor, bool)

def validar_numero(valor) -> bool:
    """Valida que el valor sea un numero real concreto (int o float finito, no bool, no nan, no inf)."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        return False
    return math.isfinite(valor)

def validar_decimal(valor) -> bool:
    """Valida que el valor sea especificamente un decimal/float real y finito (no nan, no inf)."""
    return isinstance(valor, float) and math.isfinite(valor)

def validar_negativo(valor) -> bool:
    """Valida que el valor sea un numero negativo (para resta_negativos)."""
    return validar_numero(valor) and valor < 0

def validar_lista_numerica(lista) -> bool:
    """Valida que sea una lista no vacia y que todos sus elementos sean numericos reales y finitos."""
    if not isinstance(lista, list) or len(lista) == 0:
        return False
    return all(validar_numero(elemento) for elemento in lista)

def validar_listas_misma_longitud(lista1, lista2) -> bool:
    """Valida que dos listas sean numericas y tengan el mismo tamaño (para resta_entre_listas)."""
    if not (validar_lista_numerica(lista1) and validar_lista_numerica(lista2)):
        return False
    return len(lista1) == len(lista2)

def validar_matriz(matriz) -> bool:
    """Valida que sea una matriz bien formada: lista no vacia de listas numericas no vacias, todas de igual dimension."""
    if not isinstance(matriz, list) or len(matriz) == 0:
        return False
    if not all(validar_lista_numerica(fila) for fila in matriz):
        return False
    largo_fila = len(matriz[0])
    if largo_fila == 0:
        return False
    return all(len(fila) == largo_fila for fila in matriz)

def validar_matrices_misma_dimension(m1, m2) -> bool:
    """Valida que dos matrices sean validas y tengan exactamente la misma dimension (para resta_matrices)."""
    if not (validar_matriz(m1) and validar_matriz(m2)):
        return False
    return len(m1) == len(m2) and len(m1[0]) == len(m2[0])
