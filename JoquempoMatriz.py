import random
lista = ["pedra", "papel", "tesoura"]
matrizVencedor = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
vetorPlacar = [0, 0, 0]


def atualizarPlacar(vencedor):
    vetorPlacar[vencedor] += 1


def mostraPlacar():
    print("Empates:", vetorPlacar[0])
    print("Vitórias jogador 1:", vetorPlacar[1])
    print("Vitórias jogador 2:", vetorPlacar[2])


jogo = input("Escolha Humano, Computador ou Assistir: ").lower()
print("Modo de jogo escolhido:", jogo)
continuar = True
placarJogador1 = 0
placarJogador2 = 0
while continuar:
    if jogo == "humano":
        jogada1 = input("Escolha pedra, papel ou tesoura: ").lower()
        jogada2 = input("Escolha pedra, papel ou tesoura: ").lower()
        jogadaNumerica1 = lista.index(jogada1)
        jogadaNumerica2 = lista.index(jogada2)
        vencedor = matrizVencedor[jogadaNumerica1][jogadaNumerica2]
        atualizarPlacar(vencedor)
        mostraPlacar()

    elif jogo == 'computador':
        jogada1 = input("Escolha pedra, papel ou tesoura: ").lower()
        jogada2 = random.choice(lista)
        print("O computador escolheu:", jogada2)
        jogadaNumerica1 = lista.index(jogada1)
        jogadaNumerica2 = lista.index(jogada2)
        vencedor = matrizVencedor[jogadaNumerica1][jogadaNumerica2]
        atualizarPlacar(vencedor)
        mostraPlacar()

    elif jogo == "assistir":
        print("Assistindo!")
        jogada1 = random.choice(["pedra", "papel", "tesoura"])
        jogada2 = random.choice(["pedra", "papel", "tesoura"])
        print("O computador 1 escolher:", jogada1)
        print("O computador 2 escolher:", jogada2)
        jogadaNumerica1 = lista.index(jogada1)
        jogadaNumerica2 = lista.index(jogada2)
        vencedor = matrizVencedor[jogadaNumerica1][jogadaNumerica2]
        atualizarPlacar(vencedor)
        mostraPlacar()

    else:
        print("Modo de jogo Inválido!")

    cont = input("Digite se quer continuar ou sair: ")
    if cont != 'continuar':
        continuar = False
        print("Obrigado por jogar! Feito por Pedro e Vicente.")
