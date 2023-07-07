'''
#teste
x = 10
while not (x == 0):
    x = x-1
    if x % 2 != 0:
      print (x)

terminou = False
p = i = 0
while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("P = ", p)
print ("I = ", i)
'''
# def maior_primo(numero):
#     def eh_primo(numero):
#         if numero < 2:
#             return False
#         for i in range(2, int(numero ** 0.5) + 1):
#             if numero % i == 0:
#                 return False
#         return True

#     while numero >= 2:
#         if eh_primo(numero):
#             return numero
#         numero -= 1

#     return None


# num = int(input("DIgite: "))
# maior_primo(num)

# i = 0
# while i < 3:
#   j = 0
#   while j < 3:
#     print(3*i+j+1
#           )
#     j = j + 1
# #   i = i + 1

# animais = ["gato", "cachorro", "papagaio", "arara", "jacare"]

# for x in animais:
#   print("--> ", x)

# for x in range(len(animais)):
#   print("--> ", animais[x])

# for i in range(0, 50, 5):
#   print(i)

# pares = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
# for x in range(5, 10):
#   print(pares[x])

# valores = []
# for x in range(2, 10, 2):
#     valores.append(x)
# print(valores)

# pares = []
# for i in range(1, 10):
#   if i % 2 == 0:
#     pares.append(i) 
# print(pares)

# x = pares * 3
# del (x[-1])
# print(x)

# y = x
# print(y)    
# y.append(10)
# print(x)
# print(y)

# lista1 = ["carro", "barco"]
# lista2 = lista1
# lista3 = [lista1] * 3
# lista4 = lista1 * 3

lista1 = ["carro", "barco"]
lista2 = [lista1] * 3
lista3 = lista1 * 3
lista1[1] = "metrô"

print(lista1)
print(lista2)
print(lista3)
#print(lista4)