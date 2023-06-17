import math

def funDelta(a,b,c):
    return b**2-4*a*c

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)
    

def imprime_raizes(a, b, c):

    delta = funDelta(a, b, c)

    if delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print("A unica raiz é ", x1)
    else:
        if delta < 0:
            print("esta equação não possui raizes reais")
       
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a) 
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"as raízes da equação são {x1} e {x2}")

main()