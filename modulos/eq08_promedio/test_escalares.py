import unittest
from operaciones_promedio_geometrico import promedio_geometrico_escalares


class TestPromedioGeometricoEscalares(unittest.TestCase):

    def test_numeros_positivos(self):
        self.assertAlmostEqual(promedio_geometrico_escalares([4, 9]), 6.0)

    def test_un_solo_numero(self):
        self.assertAlmostEqual(promedio_geometrico_escalares([7]), 7.0)

    def test_numero_negativo(self):
        resultado = promedio_geometrico_escalares([-8, -8])
        self.assertAlmostEqual(resultado.real, 8.0, places=5)

    def test_lista_vacia_lanza_error(self):
        with self.assertRaises(ValueError):
            promedio_geometrico_escalares([])


if __name__ == "__main__":
    unittest.main()