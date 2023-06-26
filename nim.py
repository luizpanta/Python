# NIM

# n peças na mesa inicial

# player 1 retira de 1 até max peças na rodada

# Quem tirar a ultima ganha

# Verifica quem vai iniciar a jogada
def iniciar(inicial, jogada):
    
    if (jogada + 1) % inicial == 0:
        # If n é multiplo de (m+1) computador convida o jogador a iniciar
        print("Voce começa!\n")
        return True
    else:
        # Else computador começa
        print("Computador começa!\n")
        return False


# computador_escolha_jogada(n, m)
def jogada_pc(mesa):
    if mesa > 1:
        mesa = mesa - 1
    return mesa


def jogada_usuario(mesa):
    jogada = int(input("Quantas peças você vai tirar? "))
    if valida_jogada(jogada, mesa):
        mesa = mesa - jogada
    else:
        print("Jogada invalida! Digite novamente: ")
    return mesa

def valida_jogada(jogada, mesa):
    
    if jogada < mesa:
        return jogada
    else:
        return print("Jogada invalida! Digite novamente: ")

# partida()
def partida():
    # Informa os dados de inicio
    inicio = int(input("Quantas peças? "))
    por_jogada = int(input("Limite de peças por jogada? "))    
    mesa = inicio
    max_jogada = mesa - por_jogada
    jogador = iniciar(inicio, por_jogada)
    
    # Loop do game
    while mesa > 0:
        print(f"Agora restam {mesa} peças no tabuleiro.")
        if jogador == True:
            jogada_usuario(mesa)
        else:
            jogada_pc()
        return "O computador ganhou!"
    

    

# Quantas foram removidas e quantas restam na mesa
# "O computador ganhou!"
# "Você ganhou!"


# campeonato()
def campeonato():
    # 3 partidas
    pc = 0
    jogador = 0
    for i in range(1,4):
        print(f"**** Rodada {i} ****\n")
        if partida() == "O computador ganhou!":
            pc += 1
        elif partida() == "Você ganhou!":
            jogador += 1
            
    print(f"Placar: Você {jogador} X {pc} Computador")
    
# Abertura do game
print("Bem-vindo ao jogo do NIM! Escolha: \n")

escolha = input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato\n")

if escolha == '1':
    print("Voce escolheu uma partida isolada!\n")
    partida()
elif escolha == '2':
    print("Voce escolheu um campeonato!\n")
    campeonato()
else:
    print("Opção invada.")