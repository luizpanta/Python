# Função que recebe numeros inteiros e devolve a soma
def soma_elementos(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

lista = [2, 4, 6]
print(soma_elementos(lista))