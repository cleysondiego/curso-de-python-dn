from unittest import TestCase
from collections import Counter

def conta_letras(self, string):
    return Counter(string)


class TestFrequencia(TestCase):
    def test_conta_letras_recebe_hello_e_deve_retornar_sua_contagem(self):
        entrada = 'hello'
        esperado = {'h' : 1, 'e' : 1, 'l' : 2 ,'o' : 1}
        self.assertEqual(conta_letras(entrada), esperado)

    def test_conta_letras_recebe_hello_e_deve_retornar_sua_contagem(self):
        entrada = 'python'
        esperado = {'p' : 1, 'y' : 1, 't' : 1 ,'h' : 1, 'o' : 1, 'n' : 1}
        self.assertEqual(conta_letras(entrada), esperado)