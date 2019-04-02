from Exercicio03 import conta_letras
from Exercicio04 import string_em_lista
from unittest import TestCase

def conta_frequencia_de_elementos_em_lista(input):
    lista = string_em_lista(input)
    contagem_de_letras = conta_letras(lista)
    resultado = 0
    for item in contagem_de_letras.values():
        resultado = resultado + item

    return resultado

class TestProblema5(TestCase):
    def test_conta_frequencia_de_elementos_deve_retornar_4_entrando_com_meu_nome_completo(self):
        entrada = 'Cleyson Diego da Silva'
        esperado = 4
        self.assertEqual(conta_frequencia_de_elementos_em_lista(entrada), esperado)

    def test_conta_frequencia_de_elementos_deve_retornar_2_entrnado_com_ismael_ventura(self):
        entrada = 'Ismael Ventura'
        esperado = 2
        self.assertEqual(conta_frequencia_de_elementos_em_lista(entrada), esperado)
