import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)

    numero_de_tentativas = 0

    pontos = 1000


    print("Escolha o nível de dificuldade")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Digite o número da dificuldade que deseja jogar: "))

    if (nivel == 1):
        numero_de_tentativas = 15
    elif (nivel == 2):
        numero_de_tentativas = 10
    elif (nivel == 3):
        numero_de_tentativas = 5
    else:
        print("Favor digitar um número válido 1, 2 ou 3")

    for rodada in range(1, numero_de_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, numero_de_tentativas))

        chute_str = input("Digite um número: ")
        print("Você digitou", chute_str)
        # A função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro,
        # para que a comparação com outro inteiro, no caso o numero_secreto, seja possível:
        # Realizado a criação da variável "digito" para que receba o valor da conversão.
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou! Parabéns!! O seu total de pontos foi {}!" .format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O Chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()