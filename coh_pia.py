import re
from collections import Counter

def le_assinatura():
    '''A função lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A função recebe um texto e devolve uma lista das sentenças dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A função recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A função recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez'''
    freq = Counter(lista_palavras)
    return len([palavra for palavra, frequencia in freq.items() if frequencia == 1])

def n_palavras_diferentes(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas'''
    freq = Counter(lista_palavras)
    return len(freq)

def tam_med_palavra(lista_palavras):
    '''Calcula o tamanho médio de palavra'''
    total_caracteres = sum(len(palavra) for palavra in lista_palavras)
    return total_caracteres / len(lista_palavras)

def token(lista_palavras):
    '''Calcula a relação Type-Token'''
    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)

def hapax_legomana(lista_palavras):
    '''Calcula a razão Hapax Legomana'''
    return n_palavras_unicas(lista_palavras) / len(lista_palavras)

def med_sentencas(lista_sentencas):
    '''Calcula o tamanho médio de sentença'''
    total_caracteres = sum(len(sentenca) for sentenca in lista_sentencas)
    return total_caracteres / len(lista_sentencas)

def complex_sentenca(lista_frases, lista_sentencas):
    '''Calcula a complexidade média da sentença'''
    return len(lista_frases) / len(lista_sentencas)

def med_frase(lista_frases):
    '''Calcula o tamanho médio de frase'''
    total_caracteres = sum(len(frase) for frase in lista_frases)
    return total_caracteres / len(lista_frases)

def compara_assinatura(as_a, as_b):
    '''Essa função recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # Inicialmente, calculamos a soma dos quadrados das diferenças entre os traços
    soma_diferencas_quadradas = sum((as_a[i] - as_b[i]) ** 2 for i in range(len(as_a)))

    # Calculamos a distância euclidiana
    similaridade = (soma_diferencas_quadradas) ** 0.5
    return similaridade

def calcula_assinatura(texto):
    '''Essa função recebe um texto e deve devolver a assinatura do texto.'''
    lista_palavras = separa_palavras(texto)
    lista_sentencas = separa_sentencas(texto)
    lista_frases = [frase for sentenca in lista_sentencas for frase in separa_frases(sentenca)]

    wal = tam_med_palavra(lista_palavras)  # tamanho médio de palavra
    ttr = token(lista_palavras)  # Type-Token
    hlr = hapax_legomana(lista_palavras)  # Razão Hapax Legomana
    sal = med_sentencas(lista_sentencas)  # tamanho médio de sentença
    sac = complex_sentenca(lista_frases, lista_sentencas)  # complexidade média da sentença
    pal = med_frase(lista_frases)  # tamanho médio de frase

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridade_minima = float('inf')
    texto_infectado = 0

    for i, texto in enumerate(textos):
        ass_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_texto, ass_cp)

        if similaridade < similaridade_minima:
            similaridade_minima = similaridade
            texto_infectado = i + 1  # O índice dos textos começa em 1

    return texto_infectado

if __name__ == "__main__":
    assinatura = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, assinatura)
    print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH")
