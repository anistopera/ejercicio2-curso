# Módulo de Promedio — Equipo 08

Este módulo implementa operaciones estadísticas de tendencia central:
mediana, promedio aritmético simple, promedio geométrico y moda.

## Estructura de archivos

```
modulos/eq08_promedio/
├── __init__.py               # Inicializador del paquete
├── menu.py                   # Menú interactivo con las 4 operaciones
├── operaciones_mediana.py    # Función mediana()
├── operaciones_moda.py       # Funciones calcular_moda() y obtener_datos_usuario()
├── promedio_geometrico.py    # Función promedio_geometrico()
├── promedio_simple.py        # Función promedio_simple()
├── validaciones.py           # Módulo compartido de validaciones
├── test_mediana.py           # Pruebas unitarias de mediana
├── test_promedio_simple.py   # Pruebas unitarias de promedio simple
├── test_escalares.py         # Pruebas unitarias de promedio geométrico
├── test_moda.py              # Pruebas unitarias de moda
└── README.md                 # Este archivo
```

---

## HU-801: Mediana
Autoría: Henry, Jhoan, Abby

### Descripción
La función `mediana(valores)` calcula la mediana de una lista
o matriz de números.

### Parámetros
- `valores`: una lista de números, ej. `[1, 2, 3]`,
  o una matriz (lista de listas), ej. `[[1, 2], [3, 4]]`

### Reglas de cálculo
- Cantidad impar de elementos: se devuelve el valor central
  tras ordenar.
- Cantidad par de elementos: se devuelve el promedio de los
  dos valores centrales.
- Si la entrada es una matriz, se combinan todos sus valores
  en una sola lista antes de calcular la mediana (mediana
  global, no por fila).

### Ejemplos
```python
>>> mediana([3, 1, 2])
2
>>> mediana([4, 1, 2, 3])
2.5
>>> mediana([[1, 2], [3, 4, 5]])
3
```

### Errores
La función lanza un `ValueError` si:
- La lista o matriz está vacía.
- La entrada no es una lista ni una matriz.
- Alguno de los valores no es un número.

### Notas adicionales
- **Matrices irregulares:** se admiten matrices con filas de distinto
  tamaño, ya que todos los valores se aplanan en una sola lista.
- **Tipos numéricos aceptados:** `int` y `float`. Valores booleanos,
  cadenas de texto o `None` dentro de la lista provocan `ValueError`.

---

## HU-802: Promedio Aritmético Simple

### Descripción
La función `promedio_simple(valores)` calcula el promedio aritmético
simple de una lista de números enteros o decimales.

### Fórmula
```
promedio = (x1 + x2 + ... + xn) / n
```

### Parámetros
- `valores` (list): Lista de números (`int` o `float`).

### Retorno
- `float`: El promedio aritmético de los valores.

### Ejemplos
```python
>>> promedio_simple([10, 20, 30])
20.0
>>> promedio_simple([10.5, 20.5, 30.5])
20.5
>>> promedio_simple([-10, 20, 30])
13.333333333333334
```

### Errores
- `TypeError`: Si el argumento no es una lista.
- `ValueError`: Si la lista está vacía o contiene elementos
  que no son números (solo se permiten enteros y decimales).

---

## HU-803: Promedio Geométrico

### Descripción
La función `promedio_geometrico(valores)` calcula el promedio
geométrico de una lista de números reales positivos.

### Fórmula
```
promedio = (x1 * x2 * ... * xn) ^ (1/n)
```

### Parámetros
- `valores` (list): Lista de números reales (`int` o `float`).

### Retorno
- `float`: El promedio geométrico de los valores.

### Ejemplos
```python
>>> promedio_geometrico([4, 9])
6.0
>>> promedio_geometrico([7])
7.0
>>> promedio_geometrico([2, 0, 8])
0.0
```

### Errores
- `TypeError`: Si el argumento no es una lista, si contiene
  elementos no numéricos o booleanos.
- `ValueError`: Si la lista está vacía, contiene valores
  negativos, infinitos o NaN.

### Casos especiales
- Si algún valor es `0`, el resultado es `0.0`.
- No se admiten números negativos ni complejos.

---

## HU-804: Moda

### Descripción
La función `calcular_moda(datos)` determina el valor o valores
que más se repiten en un conjunto de datos. Soporta datos numéricos
y de texto (categorías).

### Parámetros
- `datos` (list): Lista de valores (números o cadenas de texto).

### Retorno
Retorna una tupla `(resultado, tipo)`:
- Si hay moda: `resultado` es una lista con los valores modales y
  `tipo` indica la clasificación.
- Si no hay moda: `resultado` es `None` y `tipo` es un mensaje descriptivo.

### Clasificaciones
| Tipo | Descripción |
|---|---|
| Unimodal | Un solo valor se repite más |
| Bimodal | Dos valores comparten la frecuencia máxima |
| Multimodal | Tres o más valores comparten la frecuencia máxima |
| Amodal | Todos los valores tienen la misma frecuencia |

### Ejemplos
```python
>>> calcular_moda([1, 2, 2, 3, 4])
([2], 'Unimodal')
>>> calcular_moda([1, 1, 2, 2, 3])
([1, 2], 'Bimodal')
>>> calcular_moda([1, 2, 3, 4, 5])
(None, 'Amodal (no hay valor que se repita más que otro).')
>>> calcular_moda(["rojo", "azul", "rojo", "verde", "azul", "rojo"])
(['rojo'], 'Unimodal')
```

### Función auxiliar
- `obtener_datos_usuario()`: Solicita datos al usuario por consola
  separados por comas. Convierte automáticamente a `int` o `float`
  cuando es posible, y mantiene como texto lo demás.

---

## Menú Interactivo

El archivo `menu.py` ofrece un menú por consola que integra las
4 operaciones:

```
===== MENU DE PROMEDIOS =====
1. Mediana
2. Promedio aritmetico simple
3. Promedio geometrico
4. Moda
0. Salir
```

### Ejecución
```bash
python modulos/eq08_promedio/menu.py
```

---

## Cómo correr las pruebas

Desde la raíz del repositorio:

```bash
# Todas las pruebas del módulo
python -m unittest discover -s modulos/eq08_promedio -p "test_*.py" -v

# Pruebas individuales
python -m unittest modulos.eq08_promedio.test_mediana -v
python -m unittest modulos.eq08_promedio.test_promedio_simple -v
python -m unittest modulos.eq08_promedio.test_escalares -v
python -m unittest modulos.eq08_promedio.test_moda -v
```
