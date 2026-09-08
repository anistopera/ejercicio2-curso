"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: [Gabriel Torrico Nina]
"""

def resta_lista(numeros: list) -> float:
    """Resta encadenada de todos los numeros de una lista: n1 - n2 - n3 - ...

    Si la lista esta vacia, devuelve 0.
    """
    if not numeros:
        return 0

    resultado = numeros[0]
    for elemento in numeros[1:]:
        resultado -= elemento

    return resultado