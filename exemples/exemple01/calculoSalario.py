from EstacioParadigmasProgramacaoPython.exemples.exemple01.empregado import Empregado
from EstacioParadigmasProgramacaoPython.exemples.exemple01.salario import Salario

salario = Salario(10000, 700)
emp = Empregado("Miojo", 46, salario)
print(emp.salarioTotal())