import unittest
import random

def Aleatorio10():
    return random.randrange(10)

class Prueba(unittest.TestCase):

    def setUp(self):
        self.numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test(self):
        self.assertIn(Aleatorio10(), self.numeros)

    def tearDown(self):
        del(self.numeros)

unittest.main() 
