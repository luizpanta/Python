def é_hipotenusa(numero):
    a = 1
    while a < numero:
        b = a
        while b < numero:
            c = int((a**2 + b**2) ** 0.5)
            if c > numero:
                break
            if c == numero:
                return True
            b += 1
        a += 1
    return False

def soma_hipotenusas(n):
    soma = 0
    numero = 1
    while numero <= n:
        if é_hipotenusa(numero):
            soma += numero
        numero += 1
    return soma

n = int(input("Number of"))
print(é_hipotenusa(n))