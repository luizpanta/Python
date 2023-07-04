def vogal(letra):
    letra = letra.lower()
    if letra == "a":
        vogal = True
    elif letra == "e":
        vogal = True
    elif letra == "i":
        vogal = True
    elif letra == "o":
        vogal = True
    elif letra == "u":
        vogal = True
    else:
        vogal = False
    return vogal

letra = input("Digite uma letra: ")
print(vogal(letra))