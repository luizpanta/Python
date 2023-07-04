def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n -= 1
    print(fatorial)

print("Calculadora de fatorial\n")
escolha = int(input("Digite um número inteiro positivo: "))
while escolha >= 0:
    fatorial(escolha)
    escolha = int(input("Digite um número inteiro positivo: "))

            