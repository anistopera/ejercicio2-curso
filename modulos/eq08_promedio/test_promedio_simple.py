"""
Pruebas unitarias para promedio_simple.

HU-802 - Equipo 08
"""


import unittest

from .promedio_simple import promedio_simple


class TestPromedioSimple(unittest.TestCase):

    def test_promedio_enteros(self):
        resultado = promedio_simple([10, 20, 30])
        self.assertEqual(resultado, 20.0)

    def test_promedio_decimales(self):
        resultado = promedio_simple([10.5, 20.5, 30.5])
        self.assertEqual(resultado, 20.5)

    def test_promedio_negativos(self):
        resultado = promedio_simple([-10, -20, -30])
        self.assertEqual(resultado, -20.0)

    def test_promedio_positivos_y_negativos(self):
        resultado = promedio_simple([-10, 20, 30])
        self.assertEqual(resultado, 40 / 3)

    def test_un_solo_numero(self):
        resultado = promedio_simple([7])
        self.assertEqual(resultado, 7.0)

    def test_lista_vacia(self):
        with self.assertRaises(ValueError):
            promedio_simple([])

    def test_elemento_invalido(self):
        with self.assertRaises(ValueError):
            promedio_simple([10, "hola", 30])

    def test_parametro_no_es_lista(self):
        with self.assertRaises(TypeError):
            promedio_simple(10)


if __name__ == "__main__":
    unittest.main()