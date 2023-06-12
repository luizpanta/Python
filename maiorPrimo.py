num = int(input("Digite um numero maior que 2: "))

# Maior numero primo >= ao num

def primo(numero):
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

def maior_primo(numero):
    if numero >= 2:
        xxx

    else:
        print("Numero invalido")

maior_primo(num)