print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 29

rodada = 1
numero_de_tentativas = 5

while(rodada <= numero_de_tentativas):

    print("Tentativa", rodada, "de", numero_de_tentativas)
    chute = input("Digite um número: ")
    print("Você digitou ", chute)
    # A função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro,
    # para que a comparação com outro inteiro, no caso o numero_secreto, seja possível:
    # Realizado a criação da variável "digito" para que receba o valor da conversão.
    digito = int(chute)

    acertou = digito == numero_secreto
    maior   = digito > numero_secreto
    menor   = digito < numero_secreto
    stop    = digito == numero_secreto

    if(acertou):
        print("Você acertou! :)")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")