from unittest import TestCase


def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def exp(x, y, z):
    return sub(soma(x, y), z)


def expexp(x, y, z):
    return exp(exp(x, y, z), y, z)


class TestExp(TestCase):

    dummy = 1

    def test_exp_input_indireto_subtracao(self):
        self.assertEqual(exp(1, 1, self.dummy), 1)
