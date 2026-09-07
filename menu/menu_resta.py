"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: [Persona H]

Menu de la operacion de Resta, pensado para ser delegado. El menu general
del curso (main.py) podra importar y llamar a mostrar_menu() para entrar
a este modulo; al elegir "Volver", este menu retorna el control a quien
lo llamo en vez de cerrar el programa completo.

Usar SIEMPRE importaciones relativas (con puntos) -- ver nota en
tests/test_resta.py sobre por que.
"""

from ..enteros.resta_enteros import resta_enteros
from ..decimales.resta_decimales import resta_decimales
from ..validacion.validador import validar_numero

# Cada entrada: clave del menu -> (etiqueta visible, clave interna de accion)
# clave interna en None = todavia no implementada por el equipo
OPCIONES = {
    "1": ("Resta de enteros", "enteros"),
    "2": ("Resta de decimales", "decimales"),
    "3": ("Resta con negativos", None),
    "4": ("Resta encadenada de una lista", None),
    "5": ("Resta elemento a elemento entre listas", None),
    "6": ("Resta elemento a elemento entre matrices", None),
}


def _pedir_numero(mensaje: str) -> float:
    """Pide un numero por teclado hasta recibir uno valido."""
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
        except ValueError:
            print("  Entrada invalida, ingresa un numero.")
            continue
        if not validar_numero(valor):
            print("  Valor no valido.")
            continue
        return valor


def _ejecutar_enteros():
    a = int(_pedir_numero("Primer numero entero: "))
    b = int(_pedir_numero("Segundo numero entero: "))
    print(f"Resultado: {resta_enteros(a, b)}")


def _ejecutar_decimales():
    a = _pedir_numero("Primer numero decimal: ")
    b = _pedir_numero("Segundo numero decimal: ")
    print(f"Resultado: {resta_decimales(a, b)}")


# Mapa de clave interna -> funcion que la ejecuta. Cuando el equipo
# implemente negativos/lista/entre_listas/matrices, agregar aqui su
# entrada y cambiar su clave en OPCIONES de None a la nueva clave.
_ACCIONES = {
    "enteros": _ejecutar_enteros,
    "decimales": _ejecutar_decimales,
}


def mostrar_menu():
    """
    Punto de entrada del modulo de Resta.

    Disenado para ser llamado desde un menu externo (por ejemplo el
    main.py del curso, cuando delegue el modulo de resta a este equipo).
    Al elegir "Volver", retorna el control a quien lo invoco en vez de
    terminar el programa.
    """
    while True:
        print("\n=== Modulo de Resta (Bug Hunters - eq02) ===")
        for clave, (etiqueta, _) in OPCIONES.items():
            print(f"  {clave}. {etiqueta}")
        print("  0. Volver")

        eleccion = input("Elige una opcion: ").strip()

        if eleccion == "0":
            print("Saliendo del modulo de Resta...")
            return

        opcion = OPCIONES.get(eleccion)
        if opcion is None:
            print("Opcion invalida.")
            continue

        etiqueta, clave_accion = opcion
        if clave_accion is None:
            print(f"'{etiqueta}' aun no esta disponible.")
            continue

        _ACCIONES[clave_accion]()


if __name__ == "__main__":
    # Permite probar el modulo de forma independiente, sin pasar por
    # el menu general del curso.
    mostrar_menu()