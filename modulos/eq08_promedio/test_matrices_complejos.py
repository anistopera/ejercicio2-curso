import unittest
from operaciones_promedio_geometrico import promedio_geometrico_matrices


class TestPromedioGeometricoMatrices(unittest.TestCase):

    def test_matrices_reales(self):
        resultado = promedio_geometrico_matrices([[[4, 16], [9, 25]], [[1, 1], [1, 1]]])
        self.assertAlmostEqual(resultado[0][0], 2.0)
        self.assertAlmostEqual(resultado[0][1], 4.0)

    def test_matrices_complejas(self):
        resultado = promedio_geometrico_matrices([[[1 + 1j, 2]], [[1 - 1j, 8]]])
        self.assertAlmostEqual(resultado[0][1], 4.0)

    def test_dimensiones_distintas_lanza_error(self):
        with self.assertRaises(ValueError):
            promedio_geometrico_matrices([[[1, 2]], [[1, 2, 3]]])


if __name__ == "__main__":
    unittest.main()