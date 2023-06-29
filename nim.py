# NIM

# n peças na mesa inicial

# m maximo de peças por jogada

# player 1 retira de 1 até max peças na rodada

# Quem tirar a ultima ganha

def computador_escolhe_jogada(n, m):
    if n % (m + 1) != 0:
        jogada = n % (m + 1)
    else:
        jogada = m
    return jogada


def usuario_escolhe_jogada(n, m):
    
    valida_jogada = False
    
    while valida_jogada == False:
        
        jogada = input("Quantas peças você vai tirar? ")
        
        if jogada.isnumeric():
            jogada = int(jogada)
            if jogada <= m and jogada < n and jogada > 0:
                valida_jogada = True
                return jogada
            else:
                print("Oops! Jogada inválida! Tente de novo. ")
        else:
            print("Oops! Jogada inválida! Tente de novo. ")
            


# partida()
def partida():
    # Informa os dados de inicio
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m >= n:
        print("Oops! Jogada inválida! Tente de novo. ")
        m = int(input("Limite de peças por jogada? "))
        if m <= n:
            break
            
    
    if n % (m + 1) == 0:
        # If n é multiplo de (m+1) computador convida o jogador a iniciar
        print("\nVoce começa!\n")
        usuario_joga = True
    else:
        # Else computador começa
        print("\nComputador começa!\n")
        usuario_joga = False

    # Loop do game
    while n > 0:
               
        print(f"Agora restam {n} peças no tabuleiro.")
        if usuario_joga == True:
            retirar = usuario_escolhe_jogada(n, m)
            print(f"Você retirou {retirar} peças no tabuleiro.\n")
            n -= retirar
            usuario_joga = False
            
        else:
            retirar = computador_escolhe_jogada(n, m)
            print(f"O computador retirou {retirar} peças no tabuleiro.\n")
            n -= retirar
            usuario_joga =True
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            return "Fim do jogo! O computador ganhou!"
            break
    

    

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
        if partida() == "Fim do jogo! O computador ganhou!":
            print("Fim do jogo! O computador ganhou!")
            pc += 1
        elif partida() == "Você ganhou!":
            jogador += 1
    print("**** Final do campeonato! ****\n")        
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