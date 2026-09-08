import math


def promedio_geometrico(valores):
    """
    Calcula el promedio geométrico de una lista de números reales.

    Fórmula:
        (x1 * x2 * ... * xn) ** (1 / n)

    Casos especiales:
    - Lista vacía: genera ValueError.
    - Valores negativos: genera ValueError.
    - Algún valor igual a cero: devuelve 0.
    """

    if not isinstance(valores, list):
        raise TypeError("Se esperaba una lista de números")

    if len(valores) == 0:
        raise ValueError("La lista no puede estar vacía")

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Todos los elementos deben ser números reales")

        if not math.isfinite(valor):
            raise ValueError("No se permiten valores infinitos ni NaN")

        if valor < 0:
            raise ValueError(
                "El promedio geométrico no admite números negativos"
            )

    if 0 in valores:
        return 0.0

    producto = 1.0

    for valor in valores:
        producto *= valor

    return producto ** (1 / len(valores))