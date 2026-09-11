# modulos/eq05_determinante_matriz.py
# Responsable: Vicente Silvestre  (eq05)


# Responsable: Vicente Silvestre  (eq05)
def determinante_matriz(matriz):
    """Calcula el determinante de una matriz cuadrada."""
    n = len(matriz)

    if n == 1:
        return matriz[0][0]

    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    det = 0

    for columna in range(n):
        menor = [
            fila[:columna] + fila[columna + 1:]
            for fila in matriz[1:]
        ]

        det += (
            (-1) ** columna
            * matriz[0][columna]
            * determinante_matriz(menor)
        )

    return det


# Responsable: Vicente Silvestre (eq05)
def leer_matriz():
    """Lee una matriz cuadrada desde consola."""
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = []

    print()

    for i in range(n):
        fila = []

        for j in range(n):
            valor = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
            fila.append(valor)

        matriz.append(fila)

    return matriz


if __name__ == "__main__":
    matriz = leer_matriz()

    print("\nMatriz ingresada:")
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:8g}", end=" ")
        print()

    resultado = determinante_matriz(matriz)

    print(f"\nDeterminante de la matriz = {resultado:g}")