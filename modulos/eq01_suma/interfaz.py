# modulos/eq01_suma/interfaz.py
"""
HU-108 - Submenú por consola para el Equipo 01 (Suma).
Autor: Nayra Oviedo

Nota: las funciones de operaciones_suma.py (suma_lista, suma_matrices,
suma_complejos, suma_rango) están siendo desarrolladas por
los integrantes 3 a 6. Mientras no existan, se avisa en pantalla
en vez de romper el programa (ver _ejecutar).
"""

from . import operaciones_suma as op


def _pedir_float(mensaje: str) -> float:
    return float(input(mensaje))


def _leer_matriz(filas: int, columnas: int) -> list:
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = _pedir_float(f"  Elemento [{i}][{j}]: ")
            fila.append(valor)
        matriz.append(fila)
    return matriz


def _ejecutar(nombre_funcion: str, *args) -> None:
    """Ejecuta una función de operaciones_suma.py si ya fue integrada;
    si aún no existe, avisa sin detener el menú."""
    funcion = getattr(op, nombre_funcion, None)
    if funcion is None:
        print(f"\n⚠ La función '{nombre_funcion}' todavía no está disponible en operaciones_suma.py.")
        return
    try:
        resultado = funcion(*args)
        print(f"Resultado: {resultado}")
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")


def menu_equipo() -> None:
    while True:
        print("\n" + "-" * 40)
        print("     MÓDULO DE SUMA - EQUIPO 01")
        print("-" * 40)
        print(" 1. Suma de dos números")
        print(" 2. Suma de una lista de números")
        print(" 3. Suma de matrices (m x n)")
        print(" 4. Suma de números complejos")
        print(" 5. Suma de un rango (1 a N)")
        print(" 0. Volver al menú principal")
        print("-" * 40)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                a = _pedir_float("Ingrese el primer número: ")
                b = _pedir_float("Ingrese el segundo número: ")
                _ejecutar("suma_basica", a, b)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "2":
            try:
                entrada = input("Ingrese los números separados por coma (ej: 1,2,3.5): ")
                valores = [float(v.strip()) for v in entrada.split(",") if v.strip() != ""]
                _ejecutar("suma_lista", valores)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "3":
            try:
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
                print("Ingrese la Matriz A:")
                matriz_a = _leer_matriz(filas, columnas)
                print("Ingrese la Matriz B:")
                matriz_b = _leer_matriz(filas, columnas)
                _ejecutar("suma_matrices", matriz_a, matriz_b)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "4":
            try:
                print("Número complejo 1:")
                real1 = _pedir_float("  Parte real: ")
                imag1 = _pedir_float("  Parte imaginaria: ")
                print("Número complejo 2:")
                real2 = _pedir_float("  Parte real: ")
                imag2 = _pedir_float("  Parte imaginaria: ")
                c1 = complex(real1, imag1)
                c2 = complex(real2, imag2)
                _ejecutar("suma_complejos", c1, c2)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "5":
            try:
                inicio = int(input("Ingrese el inicio del rango: "))
                fin = int(input("Ingrese el fin del rango: "))
                _ejecutar("suma_rango", inicio, fin)
            except ValueError:
                print("Error: Entrada no válida.")

        elif opcion == "0":
            break

        else:
            print("Opción no válida.")