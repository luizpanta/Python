numero = int(input("Digite um número natural: "))

if n == 0:
    return 1
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
        
print("O fatorial de", numero, "é", fatorial)
