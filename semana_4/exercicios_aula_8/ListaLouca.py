class lista:
    def __init__(self, sequencia = []):
        self.sequencia = sequencia

    def __add__(self, outro_number):
        self.sequencia.append(outro_number)
        return lista(self.sequencia)

    def __neg__(self, sfs):
        self.sequencia.remove(sfs)
        return lista(self.sequencia)

    def __repr__(self):
        return str(self.sequencia)


print(lista())
print(lista() + 2 + 3 + 4)
ata = lista() + 2 + 3 + 4
print(ata)
print(ata - 2)
