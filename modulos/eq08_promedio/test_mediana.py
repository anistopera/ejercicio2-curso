"""
test_mediana.py
Pruebas unitarias de la función mediana() — HU-801, Equipo 08.
"""

import unittest
from .operaciones_mediana import mediana


class TestMediana(unittest.TestCase):

    def test_lista_impar(self):
        self.assertEqual(mediana([3, 1, 2]), 2)

    def test_lista_par(self):
        self.assertEqual(mediana([4, 1, 2, 3]), 2.5)

    def test_lista_un_solo_elemento(self):
        self.assertEqual(mediana([7]), 7)

    def test_lista_con_flotantes(self):
        self.assertEqual(mediana([1.5, 2.5, 3.5]), 2.5)

    def test_lista_con_negativos(self):
        self.assertEqual(mediana([2, -1, 5, -3, 0]), 0)

    def test_matriz_impar_total(self):
        self.assertEqual(mediana([[1, 2], [3, 4, 5]]), 3)

    def test_matriz_par_total(self):
        self.assertEqual(mediana([[1, 2], [3, 4]]), 2.5)

    def test_lista_vacia_lanza_error(self):
        with self.assertRaises(ValueError):
            mediana([])

    def test_entrada_no_numerica_lanza_error(self):
        with self.assertRaises(ValueError):
            mediana([1, "dos", 3])

    def test_entrada_no_lista_lanza_error(self):
        with self.assertRaises(ValueError):
            mediana("no es una lista")

    def test_matriz_con_valor_no_numerico_lanza_error(self):
        with self.assertRaises(ValueError):
            mediana([[1, 2], [3, "x"]])


if __name__ == "__main__":
    unittest.main()
