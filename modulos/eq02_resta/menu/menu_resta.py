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
from ..negativos.resta_negativos import resta_negativos
from ..lista.resta_lista import resta_lista
from ..entre_listas.resta_entre_listas import resta_entre_listas
from ..matrices.resta_matrices import resta_matrices
from ..validacion.validador import validar_numero

# Cada entrada: clave del menu -> (etiqueta visible, clave interna de accion)
OPCIONES = {
    "1": ("Resta de enteros", "enteros"),
    "2": ("Resta de decimales", "decimales"),
    "3": ("Resta con negativos", "negativos"),
    "4": ("Resta encadenada de una lista", "lista"),
    "5": ("Resta elemento a elemento entre listas", "entre_listas"),
    "6": ("Resta elemento a elemento entre matrices", "matrices"),
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


def _pedir_lista(mensaje: str) -> list:
    """Pide una lista de numeros separados por comas."""
    while True:
        entrada = input(mensaje)
        texto = entrada.strip()
        if not texto:
            return []
        try:
            return [float(x.strip()) for x in texto.split(",")]
        except ValueError:
            print("  Entrada invalida, usa numeros separados por comas (ej: 1,2,3).")


def _pedir_matriz(mensaje: str) -> list:
    """Pide una matriz: una fila por linea, numeros separados por comas. Linea vacia termina."""
    print(mensaje)
    print("  (una fila por linea, numeros separados por comas; linea vacia para terminar)")
    filas = []
    while True:
        entrada = input(f"  Fila {len(filas) + 1} (o Enter para terminar): ").strip()
        if not entrada:
            break
        try:
            filas.append([float(x.strip()) for x in entrada.split(",")])
        except ValueError:
            print("  Entrada invalida, usa numeros separados por comas (ej: 1,2,3).")
    return filas


def _ejecutar_enteros():
    a = int(_pedir_numero("Primer numero entero: "))
    b = int(_pedir_numero("Segundo numero entero: "))
    print(f"Resultado: {resta_enteros(a, b)}")


def _ejecutar_decimales():
    a = _pedir_numero("Primer numero decimal: ")
    b = _pedir_numero("Segundo numero decimal: ")
    print(f"Resultado: {resta_decimales(a, b)}")


def _ejecutar_negativos():
    a = _pedir_numero("Primer numero: ")
    b = _pedir_numero("Segundo numero: ")
    print(f"Resultado: {resta_negativos(a, b)}")


def _ejecutar_lista():
    numeros = _pedir_lista("Ingresa los numeros separados por comas (ej: 20,5,3): ")
    print(f"Resultado: {resta_lista(numeros)}")


def _ejecutar_entre_listas():
    lista1 = _pedir_lista("Primera lista (ej: 10,20,30): ")
    lista2 = _pedir_lista("Segunda lista (ej: 3,5,10): ")
    try:
        print(f"Resultado: {resta_entre_listas(lista1, lista2)}")
    except ValueError as e:
        print(f"  Error: {e}")


def _ejecutar_matrices():
    m1 = _pedir_matriz("Primera matriz:")
    m2 = _pedir_matriz("Segunda matriz:")
    try:
        print(f"Resultado: {resta_matrices(m1, m2)}")
    except ValueError as e:
        print(f"  Error: {e}")


# Mapa de clave interna -> funcion que la ejecuta.
_ACCIONES = {
    "enteros": _ejecutar_enteros,
    "decimales": _ejecutar_decimales,
    "negativos": _ejecutar_negativos,
    "lista": _ejecutar_lista,
    "entre_listas": _ejecutar_entre_listas,
    "matrices": _ejecutar_matrices,
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
        _ACCIONES[clave_accion]()


if __name__ == "__main__":
    # Permite probar el modulo de forma independiente, sin pasar por
    # el menu general del curso.
    mostrar_menu()