def is_prime(x):
    fator = 2
    if x == 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
    
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True
    
def n_primos(x):
    qtdade = 0
    while x > 0:
        if is_prime(x):
            qtdade += 1
        x -= 1
    return qtdade
