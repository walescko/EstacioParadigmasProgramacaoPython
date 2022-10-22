def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


n = eval(input("Entre com um valor inteiro: "))

print(f"Fatorial {n} é {factorial(n)}")
