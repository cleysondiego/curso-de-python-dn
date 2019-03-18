from unittest import TestCase, mock
from Calc import exp

print(exp(1,2,3))

class TestExp(TestCase):
    def test_input_indireto_soma(self):

        with mock.patch('Calc.add') as spy:
            exp(1,2,3)
        
        spy.assert_called_with(1,2)

        #self.assertEqual(exp(1,2,3), 0)