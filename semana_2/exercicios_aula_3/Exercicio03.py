'''
Dado o codigo:
faça assertivas em relacao ao que funciona e nao funciona nos seus casos de teste
'''
from Calc import Calc
# Testar com 0 é um teste ruim.
# Procurar PEP-008

assert Calc().soma(1, 1) == 2
assert Calc().sub(1, 1) == 0
assert Calc().mult(1, 1) == 1
assert Calc().div(1, 1) == 1
