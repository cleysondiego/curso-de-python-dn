from unittest import TestCase


def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def exp(x, y, z):
    return sub(soma(x, y), z)


class TestExp(TestCase):
    def test_exp_deve_retornar_0_com_entrada_de_1_2_3(self):
        self.assertEqual(exp(1, 2, 3), 0)

    def test_exp_deve_retornar_3_com_entrada_de_2_3_3(self):
        self.assertEqual(exp(2, 3, 3), 2)
