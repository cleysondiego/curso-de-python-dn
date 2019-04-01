from exercicio01 import soma1
from unittest import TestCase

class TestSom(TestCase):
    def test_som_com_1_deve_retornar_2(self):
        entrada = 1
        esperado = 2
        self.assertEqual(soma1(entrada), esperado)
    
    def test_som_com_10_deve_retornar_11(self):
        entrada = 10
        esperado = 11
        self.assertEqual(soma1(entrada), esperado)