"""
Operacion de promedio aritmetico simple.
HU-802 - Equipo 08
"""


def promedio_simple(valores):
    """
    Calcula el promedio aritmetico simple de una lista
    de numeros enteros o decimales.

    Args:
        valores (list): Lista de numeros.

    Returns:
        float: Promedio aritmetico.

    Raises:
        TypeError: Si no se recibe una lista.
        ValueError: Si la lista esta vacia o contiene
                    elementos que no son numeros.
    """

    if not isinstance(valores, list):
        raise TypeError("Se espera una lista de numeros")

    if len(valores) == 0:
        raise ValueError("La lista de numeros no puede estar vacia")

    for valor in valores:
        if not isinstance(valor, (int, float)):
            raise ValueError(
                f"Elemento invalido: {valor}. "
                "Solo se permiten enteros y decimales."
            )

    return sum(valores) / len(valores)