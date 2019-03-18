from unittest import TestCase

def soma (x, y):
    return x + y

def sub (x, y):
    return x - y

def exp(x, y, z):
    return sub(soma(x,y), z)

print(exp(1,2,3))

class TestExp(TestCase):
    def test_exp(self):
        self.assertEqual(exp(1,2,3), 0)