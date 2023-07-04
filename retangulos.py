largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
y = 0

while y < altura:
    x = 0
    while x < largura:        
        print("#", end="")
        x += 1
    y += 1
    print()