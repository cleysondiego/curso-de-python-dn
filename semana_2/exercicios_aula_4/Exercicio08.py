from unittest import TestCase, mock

def mocked_sabores_de_pizza():
    return [('Quatro Queijos', '29.99'), ('Frango com Catupiry', '34.99'), ('Queijo', '19.99'), ('Brócolis', '39.99')]



def pizza_com_valores(valor: float) -> list:
    resultado = []
    for pizza in mocked_sabores_de_pizza():
        if float(pizza[1]) <= valor:
            resultado.append(pizza)

    return resultado


class TestPizza(TestCase):
    def test_pizza_deve_retornar_apenas_valores_menores_que_30(self):
        entrada = 30.00
        esperado = [('Quatro Queijos', '29.99'), ('Queijo', '19.99')]
        self.assertEqual(pizza_com_valores(entrada), esperado)
