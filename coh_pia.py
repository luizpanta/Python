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
    d1 = 0
    c = 0
    while c < 6:
        d = abs(as_a[c]-as_b[c])
        c +=1
        d1 = d1 + d
    similaridade = d1/6
    return similaridade



def calcula_assinatura(texto):
    '''Essa função recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = []
    for sentenca in lista_sentencas:
        frases_separadas = separa_frases(sentenca)
        for frases in frases_separadas:
            lista_frases.append(frases)
            
    lista_palavras = []
    for frase in lista_frases:
        palavras_separadas = separa_palavras(frase)
        for palavra in palavras_separadas:
            lista_palavras.append(palavra)
    
    assinatura = []
    
    assinatura.append(tam_med_palavra(lista_palavras))
    assinatura.append(token(lista_palavras))
    assinatura.append(hapax_legomana(lista_palavras))
    assinatura.append(med_sentencas(lista_sentencas))
    assinatura.append(complex_sentenca(lista_frases, lista_sentencas))
    assinatura.append(med_frase(lista_frases))
      
    return assinatura

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
    
# def teste_automatizado():
#     print(compara_assinatura(as_a= [4.34, 0.05, 0.02, 12.81, 2.16, 0.0], as_b= [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]))
#     print(calcula_assinatura(texto="Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens."))
#     print(calcula_assinatura(texto="Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."))

# teste_automatizado()
