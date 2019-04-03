class Pessoa:
  def __init__(self, nome: str, idade: int, peso: float, altura: float):
      self.nome = nome
      self.idade = idade
      self.peso = peso
      self.altura = altura

  def envelhecer(self):
      self.idade = self.idade + 1
      crescer()

  def engordar(self, kgGanho):
      self.peso = self.peso + kgGanho

  def emagrecer(self, kgEliminados):
      self.peso = self.peso - kgEliminados

  def crescer(self):
      if self.idade < 21:
          self.altura = self.altura + 0.5


cleyson = Pessoa('Cleyson', 20, 100, 1.91)
print(cleyson.nome)
print(cleyson.idade)
print(cleyson.peso)
print(cleyson.altura)
cleyson.envelhecer
cleyson.engordar(10)
print(cleyson.nome)
print(cleyson.idade)
print(cleyson.peso)
print(cleyson.altura)
cleyson.emagrecer(30)
print(cleyson.nome)
print(cleyson.idade)
print(cleyson.peso)
print(cleyson.altura)
