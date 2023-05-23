import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2-4*a*c

if delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A unica raiz é ", x1)
else:
    if delta < 0:
        print("Está equação não possui raizes reais.\nNão pode calcular raiz negativa (delta negativo).")

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a) 
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Primeira raiz é ", x1)
        print("Segunda raiz é ", x2)