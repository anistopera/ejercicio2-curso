import cmath

def promedio_geometrico_escalares(numeros):
    """
    Calcula el promedio geometrico de una lista de escalares (reales o complejos).
    GM = (x1 * x2 * ... * xn) ** (1/n)
    """
    if not numeros:
        raise ValueError("La lista de numeros no puede estar vacia")

    n = len(numeros)
    producto = 1
    for x in numeros:
        producto *= x

    # Si el producto es negativo o complejo, se usa logaritmo complejo
    # para obtener la raiz n-esima principal correctamente
    if isinstance(producto, complex) or producto < 0:
        resultado = cmath.exp(cmath.log(producto) / n)
    else:
        resultado = producto ** (1 / n)

    return resultado


def promedio_geometrico_matrices(matrices):
    """
    Calcula el promedio geometrico elemento a elemento de una lista
    de matrices (listas de listas), reales o complejas.
    """
    if not matrices:
        raise ValueError("La lista de matrices no puede estar vacia")

    filas = len(matrices[0])
    columnas = len(matrices[0][0])

    for m in matrices:
        if len(m) != filas or any(len(fila) != columnas for fila in m):
            raise ValueError("Todas las matrices deben tener las mismas dimensiones")

    resultado = [[0] * columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            valores = [m[i][j] for m in matrices]
            resultado[i][j] = promedio_geometrico_escalares(valores)

    return resultado