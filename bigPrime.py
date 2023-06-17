def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Exemplo de uso
num = int(input("Digite um número inteiro: "))

for i in range(2, num + 1):
    if is_prime(i):
        bigPrime = i

print(bigPrime)