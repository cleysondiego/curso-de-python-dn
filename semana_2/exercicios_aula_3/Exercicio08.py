from unittest import TestCase


def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def exp(x, y, z):
    return sub(soma(x, y), z)


def expexp(x, y, z):
    return exp(exp(x, y, z), y, z)


class TestExpExp(TestCase):
    def test_expexp_deve_retornar_2_com_entrada_de_2_2_2(self):
        self.assertEqual(expexp(2, 2, 2), 2)

    def test_expexp_deve_retornar_3_com_entrada_de_3_3_3(self):
        self.assertEqual(expexp(3, 3, 3), 3)
