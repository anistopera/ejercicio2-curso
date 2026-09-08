from promedio_simple import promedio_simple
from promedio_geometrico import promedio_geometrico_escalares


def leer_lista_numeros():

    entrada = input(
        "Introduce una lista de numeros separados por coma (ej. 1,2,3,4,5): "
    )
    partes = [p.strip() for p in entrada.split(",") if p.strip() != ""]

    if not partes:
        raise ValueError("No se introdujo ningun numero")

    numeros = []
    for p in partes:
        try:
            numeros.append(int(p))
            continue
        except ValueError:
            pass
        try:
            numeros.append(float(p))
            continue
        except ValueError:
            pass
        try:
            numeros.append(complex(p))
        except ValueError:
            raise ValueError(f"'{p}' no es un numero valido")

    return numeros


def mostrar_menu():
    print("\n===== MENU DE PROMEDIOS =====")
    print("2. Promedio aritmetico simple")
    print("3. Promedio geometrico")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "0":
            print("Saliendo...")
            break

        elif opcion == "2":
            try:
                numeros = leer_lista_numeros()
                resultado = promedio_simple(numeros)
                print(f"Promedio aritmetico simple: {resultado}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                numeros = leer_lista_numeros()
                resultado = promedio_geometrico_escalares(numeros)
                print(f"Promedio geometrico: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()