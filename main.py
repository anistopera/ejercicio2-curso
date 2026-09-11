from operaciones.divisionBusquedaBinaria import divisionBusquedaBinaria


def mostrar_menu_principal() -> None:
    print("\n" + "=" * 45)
    print("        CALCULADORA - DIVISIÓN - EJERCICIO 2")
    print("=" * 45)
    print(" 1. Dividir dos números")
    print(" 0. Salir")
    print("=" * 45)


def main() -> None:
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                a = float(input("Ingrese el dividendo: "))
                b = float(input("Ingrese el divisor: "))
                cociente, residuo = divisionBusquedaBinaria(a, b)
                print(f"Cociente: {cociente}")
                print(f"Residuo: {residuo}")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "0":
            print("\nSaliendo de la aplicación...")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()