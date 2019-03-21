from unittest import TestCase
from collections import Counter

def string_em_lista(string):
    try:
        return string.split(' ')
    except:
        return "Só pode ser string"


class TestString(TestCase):
    def test_string_em_lista_deve_retornar_lista(self):
        entrada = 'Python'
        esperado = ['Python']
        self.assertEqual(string_em_lista(entrada), esperado)
    
    def test_string_em_lista_deve_retornar_lista2(self):
        entrada = 'Python love'
        esperado = ['Python', 'love']
        self.assertEqual(string_em_lista(entrada), esperado)

    def test_string_em_lista_deve_retornar_lista3(self):
        entrada = 'Python é foda'
        esperado = ['Python', 'é', 'foda']
        self.assertEqual(string_em_lista(entrada), esperado)

    def test_string_em_lista_deve_retornar_lista4(self):
        entrada = 20
        esperado = "Só pode ser string"
        self.assertEqual(string_em_lista(entrada), esperado)