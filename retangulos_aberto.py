largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
y = 0

while y < altura:
    x = 0
    while x < largura:
        if y == 0 or y == altura - 1 or x == 0 or x == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
        x += 1
    y += 1
    print()