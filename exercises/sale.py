quantidade = int(input('Qual a quantidade de mercadoria: '))
unityValue = 10.00
sale10 = 0.1
sale20 = 0.2

if (quantidade < 0):
    print("quantidade inválida")
elif (quantidade <= 10):
    valor = quantidade*unityValue
elif (quantidade > 10 and quantidade <= 20):
    valor = quantidade*unityValue*(1-sale10)
else:
    valor = quantidade*unityValue*(1-sale20)

print(f"Valor pagar por {quantidade} de produtos é R$ {valor}")