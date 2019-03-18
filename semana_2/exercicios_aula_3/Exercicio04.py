from unittest import TestCase, main
from Calc import Calc

class MinhaClasseDeTestes(TestCase):

    def setUp(self):
        self.c = Calc()
    
    def test_add(self):
        self.assertEqual(self.c.add(1,1), 2, 'Deu ruim a som')
    
    def test_sub(self):
        self.assertEqual(self.c.sub(1,1), 0, 'Deu ruim a sub')

    def test_mult(self):
        self.assertEqual(self.c.mult(2,3), 6, 'Deu ruim a mult')
    
    def test_div(self):
        self.assertEqual(self.c.div(2,2), 0, 'Deu ruim a div')


#Unidade é a menor parte do código para ser testado
#Testes de unidades são Testes que testam as menores particulas do meu codigo
'''
Testes de unidades devem ser isolados 
Não podendo conter dependencias externas

Stateless
Não se pode guardar os estados de outros testes

Unitario
Tem que testar um unico dado por vez

SUT - System Under Test (O que está sendo testado)
DOC - Componente de quem o SUT depende
CUT - Classe em teste
MUT - Metodo em teste
