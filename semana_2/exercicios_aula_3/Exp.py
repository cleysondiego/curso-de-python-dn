class Calc2:
    def soma(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def exp(self, x, y, z):
        return self.sub(self.soma(x, y), z)

    def expexp(self, x, y, z):
        return self.exp(self.exp(x, y, z), y, z)
