"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: [Persona F]
"""

def resta_matrices(m1: list, m2: list) -> list:
    """Resta elemento a elemento entre dos matrices (listas de listas)."""
    if not m1 or not m2:
        raise ValueError("Las matrices no pueden estar vacias, ingrese matrices validas ")
    if  len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Las matrices deben tener el mismo tamaño para poder restarlas ")

    resultado = []
    for i in range(len(m1)):
        fila =[]
        for j in range(len(m1[0])):
            fila.append(m1[i][j] - m2[i][j])
        resultado.append(fila)
    return resultado

    