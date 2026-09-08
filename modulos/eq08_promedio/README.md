# Módulo de Promedio — Equipo 08
 
## HU-801: Mediana
Autoría: Henry, Jhoan, Abby
 
### Descripción
La función `mediana(valores)` calcula la mediana de una lista
o matriz de números.
 
### Parámetros
- `valores`: una lista de números, ej. [1, 2, 3],
  o una matriz (lista de listas), ej. [[1, 2], [3, 4]]
 
### Reglas de cálculo
- Cantidad impar de elementos: se devuelve el valor central
  tras ordenar.
- Cantidad par de elementos: se devuelve el promedio de los
  dos valores centrales.
- Si la entrada es una matriz, se combinan todos sus valores
  en una sola lista antes de calcular la mediana (mediana
  global, no por fila).
 
### Ejemplos
>>> mediana([3, 1, 2])
2
>>> mediana([4, 1, 2, 3])
2.5
>>> mediana([[1, 2], [3, 4, 5]])
3
 
### Errores
La función lanza un ValueError si:
- La lista o matriz está vacía.
- La entrada no es una lista ni una matriz.
- Alguno de los valores no es un número.
 
### Cómo correr las pruebas
Desde la raíz del repositorio:
python -m unittest modulos.eq08_promedio.test_mediana -v
 
### Notas adicionales
- **Matrices irregulares:** se admiten matrices con filas de distinto
  tamaño (ver ejemplo `[[1, 2], [3, 4, 5]]`), ya que todos los valores
  se aplanan en una sola lista antes de calcular la mediana.
- **Tipos numéricos aceptados:** `int` y `float`. Valores booleanos,
  cadenas de texto o `None` dentro de la lista provocan `ValueError`.
