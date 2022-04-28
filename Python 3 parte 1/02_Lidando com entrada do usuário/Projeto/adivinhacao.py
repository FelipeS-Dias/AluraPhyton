print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 29

chute = input("Digite um número: ")
print("Você digitou ", chute)

# A função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro,
# para que a comparação com outro inteiro, no caso o numero_secreto, seja possível:
# Realizado a criação da variável "digito" para que receba o valor da conversão.
digito = int(chute)

if(digito == numero_secreto):
    print("Você acertou! :)")
else:
    print("Você errou, :(")

print("Fim do jogo")