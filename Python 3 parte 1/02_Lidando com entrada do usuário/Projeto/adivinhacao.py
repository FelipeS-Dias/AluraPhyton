print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 55

numero_de_tentativas = 3
rodada = 1

while(rodada <= numero_de_tentativas):
    print("Tentativa {} de {}" .format(rodada, numero_de_tentativas))

    chute_str = input("Digite um número: ")
    print("Você digitou", chute_str)
    # A função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro,
    # para que a comparação com outro inteiro, no caso o numero_secreto, seja possível:
    # Realizado a criação da variável "digito" para que receba o valor da conversão.
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou! Parabéns!!")
    else:
        if(maior):
            print("Voce errou! O chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O Chute foi menor do que o número secreto.")
    rodada = rodada + 1

print("Fim do jogo")