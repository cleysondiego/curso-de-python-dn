from unittest import TestCase, mock
import builtins

def diga_ola():
    nome = input('Me diga seu nome: ')
    print(f'Olá {nome}')


class TestIO(TestCase):
    @mock.patch('builtins.input', return_value='Cleyson')
    @mock.patch('builtins.print')
    def test_diga_ola_deve_digitar_algo(self, m_out, m_in):
        diga_ola()
        m_in.assert_called_with('Me diga seu nome: ')
        m_out.assert_called_with('Olá Cleyson')
