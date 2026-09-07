"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: [Persona F]
"""

def resta_matrices(m1: list, m2: list) -> list:
    """Resta elemento a elemento entre dos matrices (listas de listas)."""
    if  len(m1) != len(m2) or len(m1[0] != len(m2[0])):
        raise ValueError("Las matrices deben tener el mismo tamaño para poder restarlas ")

