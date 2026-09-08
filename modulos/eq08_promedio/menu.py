from promedio_simple import promedio_simple
from promedio_geometrico import promedio_geometrico
from operaciones_mediana import mediana
from operaciones_moda import calcular_moda, obtener_datos_usuario


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
        raise ValueError(f"'{p}' no es un numero valido")

    return numeros


def mostrar_menu():
    print("\n===== MENU DE PROMEDIOS =====")
    print("1. Mediana")
    print("2. Promedio aritmetico simple")
    print("3. Promedio geometrico")
    print("4. Moda")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "0":
            print("Saliendo...")
            break

        elif opcion == "1":
            try:
                numeros = leer_lista_numeros()
                resultado = mediana(numeros)
                print(f"Mediana: {resultado}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

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
                resultado = promedio_geometrico(numeros)
                print(f"Promedio geometrico: {resultado}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                datos = obtener_datos_usuario()
                resultado, tipo = calcular_moda(datos)
                if resultado is None:
                    print(f"Resultado: {tipo}")
                else:
                    print(f"Moda ({tipo}): {resultado}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()