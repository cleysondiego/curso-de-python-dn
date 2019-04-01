from unittest import TestCase, mock
from exercicio03 import diga_ola


class Stub:
    def readline(self):
        return ''


class TestDigaOla(TestCase):
    @mock.patch('builtins.input', return_values='Eduard')
    @mock.patch('builtins.print')
    def test_oi_deve_digitar_algo(self, m_out, m_in):
        diga_ola()
        m_in.assert_called_with('Me diga seu nome: ')