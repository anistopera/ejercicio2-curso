"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: Gael Olker Villarroel Sanchez
"""

def resta_entre_listas(lista1: list, lista2: list) -> list:
    """Resta elemento a elemento entre dos listas del mismo tamano."""

    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener el mismo tamano.")

    resultado = []

    for i in range(len(lista1)):
        resultado.append(lista1[i] - lista2[i])

    return resultado