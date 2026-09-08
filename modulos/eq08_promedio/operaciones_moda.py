def calcular_moda(datos):
    # Validación: lista vacía
    if not datos:
        return None, "No se ingresaron datos."

    # Contar frecuencia de cada valor
    frecuencias = {}
    for valor in datos:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1

    # Encontrar la frecuencia máxima
    max_frecuencia = max(frecuencias.values())

    # Validación: si todos los valores tienen la misma frecuencia, no hay moda
    if max_frecuencia == 1 or len(set(frecuencias.values())) == 1:
        return None, "Amodal (no hay valor que se repita más que otro)."

    # Obtener todos los valores con la frecuencia máxima
    moda = [valor for valor, freq in frecuencias.items() if freq == max_frecuencia]

    # Determinar el tipo de moda
    if len(moda) == 1:
        tipo = "Unimodal"
    elif len(moda) == 2:
        tipo = "Bimodal"
    else:
        tipo = "Multimodal"

    return moda, tipo


def obtener_datos_usuario():
    """
    Pide datos al usuario, permite números o texto (categorías).
    """
    entrada = input("Ingresa los datos separados por comas: ")
    lista = [dato.strip() for dato in entrada.split(",")]

    # Intentar convertir a número si es posible (para que 4 y "4" sean iguales)
    datos_convertidos = []
    for dato in lista:
        try:
            datos_convertidos.append(float(dato) if "." in dato else int(dato))
        except ValueError:
            datos_convertidos.append(dato)  # se queda como texto

    return datos_convertidos