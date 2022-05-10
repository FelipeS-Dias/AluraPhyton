import forca
import adivinhacao

print("*********************************")
print("**********SuperIntendo!**********")
print("*********************************")

print("Jogos Disponíveis:")
print("(1)Forca (2)Adivinhação")

jogo = int(input("Qual deseja jogar? "))

if(jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()