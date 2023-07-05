# Função devolve lista ordenada e sem elementos repetidos
def remove_repetidos(lista):
    lista_ordenada = sorted(lista)
    lista_sem_repeticoes = []
    for i in lista_ordenada:
        if i not in lista_sem_repeticoes:
            lista_sem_repeticoes.append(i)
    return lista_sem_repeticoes

lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))