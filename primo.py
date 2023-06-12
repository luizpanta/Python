numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é primo
if numero > 1:
    primo = True

    # Verificar se o número é divisível por algum outro número
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    # Imprimir o resultado
    if primo:
        print("primo")
    else:
        print("não primo")
else:
    print("não primo")
