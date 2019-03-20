from unittest import TestCase, mock


def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def exp(x, y, z):
    return sub(soma(x, y), z)


class TestExp(TestCase):
    def test_input_indireto_soma_deve_receber_x_y(self):
        x, y, z = 1, 2, 3
        with mock.patch('Exercicio11.soma') as mocked_soma:
            exp(x, y, z)

        mocked_soma.assert_called_with(x, y)

        #self.assertEqual(exp(1,2,3), 0)
    
    def test_exp_input_indireto_de_sub_deve_receber_4_z(self):
        x, y, z = 1, 2, 3
        with mock.patch('Exercicio11.sub') as mocked_sub:
            exp(x, y, z)
        
        mocked_sub.assert_called_with(3, z)