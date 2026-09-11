# operaciones/suma.py
# Responsable: Mirko Coca (eq01)

def suma_lista(valores: list[float]) -> float:
    total = 0.0
    for valor in valores:
        total += valor
    return total