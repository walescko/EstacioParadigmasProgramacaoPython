nota = float(input('Entre com a nota (0.0 a 10.0): '))

if (nota < 0 or nota > 10):
    resultado = "nota invalida."
elif (nota >=7):
    resultado = "Aprovado"
elif (nota >=5 or nota < 7):
    resultado = "Em exame"
else:
    resultado = "reprovado!"

print(f'O aluno está {resultado}.')