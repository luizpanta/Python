def MinMax(temperaturas):
    print(" A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print(" A maior temperatura do mês foi: ", maxima(temperaturas), "C.")

def minima(temps):
    # min = 0 em teste corrigido para
    min = temps[0]
    i = 0
    while i < len(temps):
        if  temps[i] < min:
            min = temps[i]
        i += 1
    return min

def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if  temps[i] > max:
            max = temps[i]
        i += 1

def teste_pontual(temps, valor_esperado):
    valor_calculado = minima(temps)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temps)
        print("Valor esperado para array", valor_esperado, ". Valor calculado", valor_calculado)
        
def testa_minima(): # Refatorar para uma matriz
    print("Iniciando testes.")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0,], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6], 0)
    teste_pontual([12, 23, 35, 25, 8], 8)
    teste_pontual([-15, 22, 34, 13, 6], -15)
    print("Finalizado testes.")