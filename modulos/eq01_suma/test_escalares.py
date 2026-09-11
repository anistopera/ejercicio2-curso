
from modulos.eq01_suma.operaciones_suma import suma_lista
def test_suma_lista():
    assert suma_lista([1.0, 2.0, 3.0]) == 6.0

def test_suma_lista_decimales():
    assert suma_lista([1.5, 2.5, 3.0]) == 7.0

def test_suma_lista_vacia():
    assert suma_lista([]) == 0.0

def test_suma_lista_negativos():
    assert suma_lista([-5.0, 10.0, -2.0]) == 3.0