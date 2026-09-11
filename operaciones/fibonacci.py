# operaciones/fibonacci.py

def fibonacci(n):
    """
    Responsable: Ian Nicolás Flores Candia (eq06)
    Descripción: Devuelve el n-ésimo número de la sucesión de Fibonacci
                 usando un enfoque iterativo.
    """
    if not isinstance(n, int):
        raise TypeError("El índice debe ser un número entero")
    if n < 0:
        raise ValueError("El índice no puede ser negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a