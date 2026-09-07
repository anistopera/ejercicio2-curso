import modulos.eq01_suma.interfaz as eq01_suma

def mostrar_menu_principal() -> None:
    print("\n" + "=" * 45)
    print("   CALCULADORA COLABORATIVA MULTI-EQUIPO")
    print("=" * 45)
    print(" 1. Operaciones de Suma (Equipo 01)")
    print(" 2. Operaciones de Resta (Equipo 02 - Pendiente)")
    print(" 0. Salir")
    print("=" * 45)

def main() -> None:
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            eq01_suma.menu_equipo()
        elif opcion == "0":
            print("\nSaliendo de la aplicación...")
            break
        else:
            print("\nOpción no válida o módulo no integrado aún.")

if __name__ == "__main__":
    main()
