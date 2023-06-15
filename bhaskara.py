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
        print("esta equação não possui raizes reais")

    #elif x1 == x2:
        #print("a raiz dupla desta equação é ", x1)
    
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a) 
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"as raízes da equação são {x1} e {x2}")