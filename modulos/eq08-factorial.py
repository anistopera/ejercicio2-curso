def factorial_escalar(n):
    """
    Calcula el factorial de un entero no negativo n.
    n! = n * (n-1) * (n-2) * ... * 1   (0! = 1 por definición)
    """
    if not float(n).is_integer():
        raise ValueError(f"El factorial solo está definido para enteros. Se recibió: {n}")

    n = int(n)

    if n < 0:
        raise ValueError(f"El factorial no está definido para números negativos. Se recibió: {n}")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado