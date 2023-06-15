def verificar_ordem_crescente():
    numeros = []
    
    for i in range(3):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)
    
    # Verificar se os números estão em ordem crescente
    em_ordem_crescente = all(numeros[i] <= numeros[i+1] for i in range(len(numeros)-1))
    
    if em_ordem_crescente:
        print("crescente")
    else:
        print("não está em ordem crescente")

# Chamando a função para executar o algoritmo
verificar_ordem_crescente()
