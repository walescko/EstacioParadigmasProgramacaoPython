class People:
    _contador = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        People._contador += 1
    def imprimir(self):
        print(self.nome, " tem ", self.idade)

    @property
    def contador(self):
        return type(self)._contador

p1 = People("Charles", 21)
print(p1.contador)
print(People._contador)