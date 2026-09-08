import unittest


from ..enteros.resta_enteros import resta_enteros
from ..decimales.resta_decimales import resta_decimales
from ..negativos.resta_negativos import resta_negativos
from ..lista.resta_lista import resta_lista
from ..entre_listas.resta_entre_listas import resta_entre_listas
from ..matrices.resta_matrices import resta_matrices
from ..validacion.validador import validar_numero, validar_lista_numerica

class TestRestaBugHunters(unittest.TestCase):

    def test_resta_enteros(self):
        self.assertEqual(resta_enteros(15, 5), 10)
        self.assertEqual(resta_enteros(0, 8), -8)
        self.assertEqual(resta_enteros(10, 10), 0)

    def test_resta_decimales(self):
        self.assertAlmostEqual(resta_decimales(10.5, 3.2), 7.3, places=2)
        self.assertAlmostEqual(resta_decimales(5.0, 2.55), 2.45, places=2)
        self.assertAlmostEqual(resta_decimales(0.0, 1.1), -1.1, places=2)

    def test_resta_negativos(self):
        self.assertEqual(resta_negativos(-10, -5), -5)
        self.assertEqual(resta_negativos(-3, 7), -10)
        self.assertEqual(resta_negativos(5, -4), 9)
        self.assertEqual(resta_negativos(-5, -5), 0)

    def test_resta_lista(self):
        self.assertEqual(resta_lista([20, 5, 3]), 12)
        self.assertEqual(resta_lista([100, 50, 25, 25]), 0)
        self.assertEqual(resta_lista([10]), 10)
        self.assertEqual(resta_lista([]), 0) 

    def test_resta_entre_listas(self):
        self.assertEqual(resta_entre_listas([10, 20, 30], [3, 5, 10]), [7, 15, 20])
        self.assertEqual(resta_entre_listas([0, 0], [1, 1]), [-1, -1])
        self.assertEqual(resta_entre_listas([-5, 10], [-2, 5]), [-3, 5])

    def test_resta_matrices(self):
        m1 = [[5, 8], [3, 6]]
        m2 = [[2, 3], [1, 4]]
        esperado = [[3, 5], [2, 2]]
        self.assertEqual(resta_matrices(m1, m2), esperado)

    def test_validar_numero(self):
        self.assertTrue(validar_numero(5))
        self.assertTrue(validar_numero(-3.14))
        self.assertTrue(validar_numero(0))
        self.assertFalse(validar_numero("texto"))
        self.assertFalse(validar_numero(None))

    def test_validar_lista_numerica(self):
        self.assertTrue(validar_lista_numerica([1, 2.5, -3]))
        self.assertFalse(validar_lista_numerica([1, "dos", 3]))
        self.assertFalse(validar_lista_numerica(["1", "2"]))

if __name__ == '__main__':
    unittest.main()