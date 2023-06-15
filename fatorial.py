numero = int(input("Digite um número natural: "))

def fatorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial
        
fatorial = fatorial(numero)
print(fatorial)
