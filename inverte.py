# Função que recebe lista e inverte a ordem
def inverte_lista(lista):
    nova_lista = []
    for item in range(len(lista)):
        new = len(lista) - item - 1
        nova_lista.append(lista[new])
        new -= 1
    return nova_lista

def nova_lista(items):
    lista = []
    lista.append(items)
    return lista

entrada = 1
while entrada > 0:
    entrada = int(input("Digite um número: "))
    lista = nova_lista(entrada)
    invertida = inverte_lista(lista)
for i in invertida:
    print(i)