def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Exemplo de uso
num = int(input("Digite um número inteiro: "))

print(is_prime(num))