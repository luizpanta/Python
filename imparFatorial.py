numero = int(input("Digite o valor de n: "))

def fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

n = 0
contador = 0

while contador < numero:
    n += 1
    if n % 2 != 0:
        print(fatorial(n))
        contador += 1