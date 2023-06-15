def verifica_digito_adjacente(numero):
    numero_str = str(numero)  # Converte o número para uma string
    
    for i in range(len(numero_str) - 1):
        if numero_str[i] == numero_str[i+1]:
            return True  # Retorna True se encontrar dígitos adjacentes iguais
    
    return False  # Retorna False se não encontrar dígitos adjacentes iguais

# Exemplo de uso:
numero = int(input("Digite um número: "))
resultado = verifica_digito_adjacente(numero)

if resultado:
    print("sim")
else:
    print("não")
