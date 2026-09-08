"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: [Belen Grageda]
"""


def resta_negativos(a: float, b: float) -> float:
    """
    Resta con manejo explicito de numeros negativos: a - b.

    Ejemplos:
        resta_negativos(-10, -5)  -> -5
        resta_negativos(-3, 7)    -> -10
        resta_negativos(5, -4)    -> 9
    """
    resultado = a - b
    return resultado


if __name__ == "__main__":
    # Permite probar el modulo de forma independiente, sin pasar por el
    # menu general. No se usa desde el resto del proyecto -- ahi siempre
    # se llama a resta_negativos(a, b) directamente.
    print("--- RESTA ENTRE NUMEROS NEGATIVOS ---")
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    resultado = resta_negativos(num1, num2)

    print("\n--- Desglose de la operacion ---")
    print(f"Expresion inicial : {num1} - ({num2})")
    print(f"Aplicando signos   : {num1} + {-num2}")
    print(f"Resultado final    : {resultado}")

    if resultado < 0:
        print("El resultado final es NEGATIVO.")
    elif resultado > 0:
        print("El resultado final es POSITIVO.")
    else:
        print("El resultado es CERO.")
