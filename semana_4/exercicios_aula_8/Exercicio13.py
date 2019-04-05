from unittest import TestCase


class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def retornarNome(self):
        return self.nome

    def retornarSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        return (self.salario * (percentualDeAumento/100)) + self.salario


class TestFuncionario(TestCase):
    def test_funcionario_deve_retornar_cleyson_e_1000(self):
        nome = 'Cleyson'
        salario = 1000
        obj = Funcionario('Cleyson', 1000)
        self.assertEqual(obj.retornarNome(), nome)
        self.assertEqual(obj.retornarSalario(), salario)


if __name__ == '__main__':
    harry = Funcionario('Harry', 25000)
    print(harry.aumentarSalario(10))
