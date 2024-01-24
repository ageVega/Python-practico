import unittest
import Operaciones

class Pruebas(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(Operaciones.Sumar(3,4),7)
    def test_resta(self):
        self.assertEqual(Operaciones.Restar(33,17),16)
    def test_multiplicar(self):
        self.assertEqual(Operaciones.Multiplicar(12,4),48)
    def test_dividir(self):
        self.assertEqual(Operaciones.Dividir(33,3),11)
    def test_potencia(self):
        self.assertEqual(Operaciones.Potencia(3,3),27)
    def test_factorial(self):
        self.assertEqual(Operaciones.Factorial(5),120)

unittest.main()
