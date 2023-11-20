  # test_suma.py

import unittest
from suma import sumar, restar, multiplicar, dividir

class TestOperacionesMatematicas(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    """
    def test_restar(self):
        # Agrega pruebas para la función restar
        pass

    def test_multiplicar(self):
        # Agrega pruebas para la función multiplicar
        pass

    def test_dividir(self):
        # Agrega pruebas para la función dividir
        pass
    """

if __name__ == '__main__':
    unittest.main()
