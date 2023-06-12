num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

def maximo(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

if num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")