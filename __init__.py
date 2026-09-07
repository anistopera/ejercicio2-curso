"""
Equipo: Bug Hunters (eq02)
Modulo de Resta - punto de conexion central del equipo.

Este archivo reune las funciones de todas las sub-carpetas para que
el resto del proyecto (main.py general del curso) pueda hacer:

    from modulos.eq02_resta import resta_enteros, resta_decimales, ...

en vez de tener que conocer la carpeta interna de cada funcion.

IMPORTANTE: cada persona descomenta su propia linea de importacion
una vez que su funcion este implementada (no antes, para evitar
errores de importacion mientras el archivo aun esta vacio).

Estas importaciones usan puntos (relativas), no rutas absolutas tipo
"modulos.eq02_resta.enteros...". Esto es a proposito: las relativas
siguen funcionando sin cambios aunque esta carpeta se mueva de lugar
(por ejemplo, cuando migremos todo dentro de modulos/eq02_resta/ en
el repo oficial del curso).
"""

from .enteros.resta_enteros import resta_enteros
from .decimales.resta_decimales import resta_decimales
# from .negativos.resta_negativos import resta_negativos
# from .lista.resta_lista import resta_lista
# from .entre_listas.resta_entre_listas import resta_entre_listas
# from .matrices.resta_matrices import resta_matrices
from .validacion.validador import validar_numero, validar_lista_numerica
from .menu.menu_resta import mostrar_menu