class SumaCuadrados:
    """
    Clase para calcular la suma de cuadrados de números.
    """

    def calcular(self, numeros):
        """
        Recibe una lista de números y retorna la suma de sus cuadrados.
        Ejemplo: [1, 2, 3] -> 1^2 + 2^2 + 3^2 = 14
        """
        if not isinstance(numeros, list) or len(numeros) == 0:
            raise ValueError("Debes ingresar una lista de números no vacía.")

        for n in numeros:
            if not isinstance(n, (int, float)):
                raise ValueError(f"'{n}' no es un número válido.")

        return sum(n ** 2 for n in numeros)


# Ejemplo de uso
if __name__ == "__main__":
    operacion = SumaCuadrados()
    numeros = [1, 2, 3, 4]
    resultado = operacion.calcular(numeros)
    print(f"La suma de cuadrados de {numeros} es: {resultado}")