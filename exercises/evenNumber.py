numbersList = [10, 2, 5, 7, 6, 3]
sumEvens = 0
n = len(numbersList)

for i in range(n):
    if numbersList[i] % 2 == 0:
        sumEvens += numbersList[i]

print(f"A soma dos pares da lista é {sumEvens}.")
