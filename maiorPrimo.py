def éPrimo(numero):

    primo = False

    if numero % 2 == 0 or numero % 3 == 0 or numero % 4 == 0 or numero % 5 == 0 or numero % 6 == 0 or numero % 7 == 0:
        primo = False
        if numero % numero == 0:
            primo = False
        
        elif numero > 1 and numero == 2 or numero == 3 or numero == 5 or numero == 7:
            primo = True

    else:
        primo = True

    return primo

def maior_primo(numero):

    for i in range(2, numero + 1):
        if éPrimo(i):
            maior_primo = i
    return maior_primo

num = int(input("Digite um numero maior que 2: "))

if num <= 2:
    print("Invalido")

print(maior_primo(num))