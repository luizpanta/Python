meuCartao = int(input("Digite o numero do seu cartao: "))

cartaoLido = 1
meuCartaoNaLista = False

while cartaoLido != 0 and not meuCartaoNaLista:
    cartaoLido = int(input("Digite o proximo cartao: "))
    if cartaoLido == meuCartao:
        meuCartaoNaLista = True

if meuCartaoNaLista:
    print("Meu cartao na lista")
else:
    print("Não esta na lista")