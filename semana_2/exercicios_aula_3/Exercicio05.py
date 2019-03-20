'''
DOC da div = Classe CalcS
'''

from Calc import Calc
from unittest import TestCase


class TestsCalcSoma(TestCase):
    def test_soma_deve_retornar_2_com_entrada_de_1_1(self):
        c = Calc()
        self.assertEqual(c.soma(1, 1), 2)


class TestsCalcSub(TestCase):
    def test_sub_deve_retornar_0_com_entrada_de_1_1(self):
        c = Calc()
        self.assertEqual(c.sub(1, 1), 0)


class TestsCalcMult(TestCase):
    def test_mult_deve_retornar_50_com_entrada_de_10_5(self):
        c = Calc()
        self.assertEqual(c.mult(10, 5), 50)


class TestsCalcDiv(TestCase):
    def test_div_deve_retornar_5_com_entrada_de_10_2(self):
        c = Calc()
        self.assertEqual(c.div(10, 2), 5)
