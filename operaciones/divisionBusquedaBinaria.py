# operaciones.divisionBusquedaBinaria.py
# Responsable: Natalie Saravia Camacho (eq07)

def divisionBusquedaBinaria(dividendo: float, divisor: float):
    """
    Divide 'dividendo' entre 'divisor' usando búsqueda binaria
    sobre el posible cociente.

    Retorna una tupla (cociente, residuo).
    """
    if divisor == 0:
        raise ValueError("No se puede dividir entre cero")

    # Determinar el signo del resultado
    signo = 1
    if (dividendo < 0) != (divisor < 0):
        signo = -1

    dividendo = abs(dividendo)
    divisor = abs(divisor)

    izquierda, derecha = 0, int(dividendo)
    cociente = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if divisor * medio <= dividendo:
            cociente = medio
            izquierda = medio + 1
        else:
            derecha = medio - 1

    residuo = dividendo - (divisor * cociente)

    return cociente * signo, residuo