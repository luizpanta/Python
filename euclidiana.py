import math

# Receber as coordenadas dos dois pontos
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calcular a distância entre os dois pontos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Verificar se a distância é maior ou igual a 10 e imprimir o resultado
if distancia >= 10:
    print("Longe")
else:
    print("Perto")
