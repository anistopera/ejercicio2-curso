import unittest
from unittest.mock import patch
from operaciones_moda import *


class TestCalcularModa(unittest.TestCase):

    def test_lista_vacia(self):
        resultado, mensaje = calcular_moda([])
        self.assertIsNone(resultado)
        self.assertEqual(mensaje, "No se ingresaron datos.")

    def test_amodal_todos_unicos(self):
        # Todos aparecen 1 vez
        resultado, mensaje = calcular_moda([1, 2, 3, 4, 5])
        self.assertIsNone(resultado)
        self.assertEqual(
            mensaje, "Amodal (no hay valor que se repita más que otro)."
        )

    def test_amodal_misma_frecuencia_mayor_a_uno(self):
        # Todos los elementos aparecen exactamente 2 veces
        resultado, mensaje = calcular_moda([1, 1, 2, 2, 3, 3])
        self.assertIsNone(resultado)
        self.assertEqual(
            mensaje, "Amodal (no hay valor que se repita más que otro)."
        )

    def test_unimodal_numerica(self):
        resultado, tipo = calcular_moda([1, 2, 2, 3, 4])
        self.assertEqual(resultado, [2])
        self.assertEqual(tipo, "Unimodal")

    def test_bimodal_numerica(self):
        resultado, tipo = calcular_moda([1, 1, 2, 2, 3])
        self.assertCountEqual(resultado, [1, 2])
        self.assertEqual(tipo, "Bimodal")

    def test_multimodal_numerica(self):
        resultado, tipo = calcular_moda([1, 1, 2, 2, 3, 3, 4])
        self.assertCountEqual(resultado, [1, 2, 3])
        self.assertEqual(tipo, "Multimodal")

    def test_datos_tipo_texto(self):
        datos = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]
        resultado, tipo = calcular_moda(datos)
        self.assertEqual(resultado, ["rojo"])
        self.assertEqual(tipo, "Unimodal")

    def test_datos_mixtos_y_flotantes(self):
        datos = [2.5, 2.5, "manzana", 10]
        resultado, tipo = calcular_moda(datos)
        self.assertEqual(resultado, [2.5])
        self.assertEqual(tipo, "Unimodal")


class TestObtenerDatosUsuario(unittest.TestCase):

    @patch("builtins.input", return_value="1, 2, 3, 4")
    def test_enteros_con_espacios(self, mock_input):
        resultado = obtener_datos_usuario()
        self.assertEqual(resultado, [1, 2, 3, 4])

    @patch("builtins.input", return_value="1.5, 2, 3.75")
    def test_flotantes_y_enteros(self, mock_input):
        resultado = obtener_datos_usuario()
        self.assertEqual(resultado, [1.5, 2, 3.75])

    @patch("builtins.input", return_value="rojo, verde, azul")
    def test_cadenas_de_texto(self, mock_input):
        resultado = obtener_datos_usuario()
        self.assertEqual(resultado, ["rojo", "verde", "azul"])

    @patch("builtins.input", return_value="10, texto, 3.14, perro")
    def test_datos_mixtos(self, mock_input):
        resultado = obtener_datos_usuario()
        self.assertEqual(resultado, [10, "texto", 3.14, "perro"])


if __name__ == "__main__":
    unittest.main(verbosity=2)