def validar_lista_numeros(numeros):
    if not isinstance(numeros, list) or len(numeros) == 0:
        raise ValueError("Se espera una lista no vacia de numeros")
    for x in numeros:
        if not isinstance(x, (int, float, complex)):
            raise ValueError(f"Elemento invalido: {x}")
    return True


def validar_matrices_mismas_dimensiones(matrices):
    if not matrices:
        raise ValueError("Se espera una lista no vacia de matrices")
    filas = len(matrices[0])
    columnas = len(matrices[0][0]) if filas > 0 else 0
    for m in matrices:
        if len(m) != filas or any(len(f) != columnas for f in m):
            return False
    return True