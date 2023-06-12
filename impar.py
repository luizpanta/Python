numero = int(input("Digite o valor de n: "))

n = 0
contador = 0

while contador < numero:
    n += 1
    if n % 2 != 0:
        print(n)
        contador += 1