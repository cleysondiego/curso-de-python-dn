class lista:
    def __init__(self, sequencia = []):
        self.listaa = sequencia

    def __add__(self, outro_number):
        self.listaa.append(outro_number)
        return lista(self.listaa)
    
    def __neg__(self, sfs):
        self.listaa.remove(self.listaa.find(sfs))
        return lista(self.listaa)
    
    def __repr__(self):
        return str(self.listaa)


print(lista())
print(lista() + 2 + 3 + 4)
ata = lista() + 2 + 3 + 4
print(lista() - 2)
