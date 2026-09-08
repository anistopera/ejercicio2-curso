import unittest
from modulos.eq08_promedio.promedio_geometrico import promedio_geometrico


class TestPromedioGeometricoEscalares(unittest.TestCase):

    def test_numeros_positivos(self):
        self.assertAlmostEqual(promedio_geometrico([4, 9]), 6.0)

    def test_un_solo_numero(self):
        self.assertAlmostEqual(promedio_geometrico([7]), 7.0)

    def test_numero_negativo(self):
        with self.assertRaises(ValueError):
            promedio_geometrico([-8, -8])

    def test_con_cero(self):
        self.assertEqual(promedio_geometrico([2, 0, 8]), 0.0)

    def test_lista_vacia_lanza_error(self):
        with self.assertRaises(ValueError):
            promedio_geometrico([])

    def test_elemento_no_numerico(self):
        with self.assertRaises(TypeError):
            promedio_geometrico([4, "texto"])

    def test_argumento_no_es_lista(self):
        with self.assertRaises(TypeError):
            promedio_geometrico("4, 9")

    def test_booleano_no_permitido(self):
        with self.assertRaises(TypeError):
            promedio_geometrico([True, 9])


if __name__ == "__main__":
    unittest.main()