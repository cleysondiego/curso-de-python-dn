from unittest import TestCase


def write_data(data: str) -> str:
    arquivo = open('Exercicio07.txt', 'w')
    arquivo.writelines(data)
    arquivo.close()


class TestWriteData(TestCase):
    def test_write_data_deve_escrever_cleyson_no_arquivo_quando_entrar_com_cleyson(self):
        entrada = 'Cleyson'
        write_data(entrada)
        result = open('Exercicio07.txt', 'r')
        self.assertEqual(result.readline(), entrada)
        result.close()
