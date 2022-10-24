class inheritance:
    def __init__(self,a , b,):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def multiplicate(self):
        return self.a*self.b

class devirateInheritance(inheritance):
    def subtract(self):
        return self.a-self.b
    def division(self):
        return self.a/self.b

a = 40
b = 20
d = devirateInheritance(a, b)
print(f'soma: {a} + {b} = {d.sum()}')
print(f'Subtração: {a} - {b} = {d.subtract()}')
print(f'multiplicação: {a} * {b} = {d.multiplicate()}')
print(f'Divisão: {a}/{b} = {d.division()}')

