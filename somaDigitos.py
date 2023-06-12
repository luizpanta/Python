numero = int(input("Digite um número inteiro: "))
soma = 0

# Loop para calcular a soma dos dígitos
while numero > 0:
    digito = numero % 10  # Obtém o último dígito
    soma += digito       # Acumula o dígito na soma
    numero //= 10        # Remove o último dígito do número

print("A soma dos dígitos é:", soma)