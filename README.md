# Modulo Resta — Equipo Bug Hunters (eq02)

## Estructura

```
eq02_resta/
├── __init__.py          <- Conecta todas las funciones (descomentar tu import cuando termines)
├── enteros/              -> Persona A: resta_enteros(a, b)
├── decimales/            -> Persona B: resta_decimales(a, b)
├── negativos/            -> Persona C: resta_negativos(a, b)
├── lista/                -> Persona D: resta_lista(numeros)
├── entre_listas/         -> Persona E: resta_entre_listas(lista1, lista2)
├── matrices/             -> Persona F: resta_matrices(m1, m2)
├── validacion/           -> Persona G: validar_numero(valor), validar_lista_numerica(lista)
├── menu/                 -> Persona H: mostrar_menu()
└── tests/                -> Persona I: test_resta.py
```

## Como trabajar tu parte

1. Entra SOLO a tu carpeta asignada (no edites archivos de otras carpetas)
2. Implementa tu funcion reemplazando el `pass` / `TODO`
3. Una vez que tu funcion funcione, descomenta tu linea correspondiente en el `__init__.py` de la raiz de este modulo
4. Haz commit siguiendo la convencion: `feat(eq02): [HU201] descripcion en presente`
5. Sube tu rama y abre el Pull Request hacia `integration/eq02`

## Convencion de ramas

`<prefijo>/eq02-HU201-<descripcion-corta>`

Ejemplo: `feature/eq02-HU201-resta-enteros`

## Integracion (a cargo del Git Leader)

El menu (`menu/menu_resta.py`) y el `__init__.py` son los unicos archivos
que van a requerir cambios de mas de una persona -> normal que generen
conflictos, es parte del ejercicio. Avisar al Git Leader antes de mergear
cambios grandes en estos dos archivos.
