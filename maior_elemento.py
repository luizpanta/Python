# Função que retorna o maior numero inteiro de uma lista
def maior_elemento(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior

lista = [1, 2, 3, 4, 11, 6, 7, 8, 9]
print(maior_elemento(lista))