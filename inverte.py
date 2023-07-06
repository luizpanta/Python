# Função que recebe lista e inverte a ordem
def inverte_lista(lista):
    nova_lista = []
    for item in lista:
        nova_lista.append(item)



def inverte(lista):
    nova_lista = []
    for i in range(len(lista)):
        nova_lista.append(lista[nova_lista.index(lista[i])])
    return nova_lista

lista = [1,2,3,4,5,6,7,8,]
print(inverte(lista))