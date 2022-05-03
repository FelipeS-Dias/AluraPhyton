print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 55

numero_de_tentativas = 3

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
        print("Voce acertou! Parabéns!!")
        break
    else:
        if(maior):
            print("Voce errou! O chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O Chute foi menor do que o número secreto.")

print("Fim do jogo")