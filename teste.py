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

i = 0
while i < 3:
  j = 0
  while j < 3:
    print(3*i+j+1
          )
    j = j + 1
  i = i + 1