import random

tabuleiro = [" "] * 9
cpu = False
jogador_atual = ""
vencedor = False

def desenha_tabuleiro():
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

def escolhe_jogador():
    global jogador_atual,cpu
    # cpu ou jogador
    choice = input("Você quer jogar contra o computador? (S/N): ").upper()
    while choice not in ["S", "N"]:
        choice = input("Você quer jogar contra o computador? (S/N): ").upper()
    if choice == "S":
        cpu = True
    else:
        cpu = False
    jogador_atual = "O" if jogador == "X" else "X"

def faz_jogada(jogador_atual):
    global vencedor

    while True:
        if not cpu:
            jogada = input("Jogador " + jogador_atual + ", escolha uma posição (1-9): ")
        else:
            if jogador_atual == jogador:
                jogada = input("Jogador " + jogador_atual + ", escolha uma posição (1-9): ")
            else:
                jogada = str(random.randint(1, 9))
                if tabuleiro[int(jogada) - 1] != " ":
                    jogada = str(random.randint(1, 9))
                print("O computador escolheu a posição " + jogada)

        jogada = int(jogada) - 1

        if tabuleiro[jogada] == " ":
            tabuleiro[jogada] = jogador_atual
            break
        else:
            print("Posição já ocupada, escolha outra.")

    vitorias = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    if any(all(tabuleiro[pos] == jogador for pos in vitoria) for vitoria in vitorias):
        vencedor = True
    else:
        vencedor = False

def troca_jogador():
    global jogador_atual

    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"

def jogar():
    global vencedor

    escolhe_jogador()

    while not vencedor:
        troca_jogador()
        desenha_tabuleiro()
        faz_jogada(jogador_atual)

    desenha_tabuleiro()
    if jogador_atual == jogador:
        print("Parabéns, jogador " + jogador + ", você venceu!")
    else:
        print("O computador venceu!")


if __name__ == "__main__":
    jogador = input("Escolha X ou O para jogar: ").upper()
    while jogador not in ["X", "O"]:
        jogador = input("Escolha X ou O para jogar: ").upper()
    jogar()
