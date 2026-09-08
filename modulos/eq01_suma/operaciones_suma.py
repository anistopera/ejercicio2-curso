def suma_matrices(matriz_a, matriz_b):
    if len(matriz_a) != len(matriz_b):
        raise ValueError("Las matrices deben tener el mismo número de filas")

    if len(matriz_a[0]) != len(matriz_b[0]):
        raise ValueError("Las matrices deben tener el mismo número de columnas")

    resultado = []

    for i in range(len(matriz_a)):
        fila = []

        for j in range(len(matriz_a[0])):
            suma = matriz_a[i][j] + matriz_b[i][j]
            fila.append(suma)

        resultado.append(fila)

    return resultado