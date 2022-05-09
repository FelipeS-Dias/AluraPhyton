print("------------")
print("Atividade 15")
print("------------")

import random

# sorteado = random.randrange(0,4) Favorece a Tamires dois números
sorteado = random.randrange(1,4) # Sorteio justo entre os 3

print(sorteado)

if (sorteado == 1):
    print("Parabéns Paulo você é o vencedor")
elif (sorteado == 2):
    print("Parabéns Juliana você é a vencedora")
else:
    print("Parabéns Tamires você é a vencedora")

# O Exercicio era para identificar porque a Tamires tinha mais chances do que os outros de vencer o sorteio.

# A verdade é que o sorteio não foi justo pois a Tamires realmente tinha mais chance de ganhar!
# A função random.randrange nos retorna um número no intervalo especificado.
# Nesse exemplo, temos como saída os possíveis valores 0, 1, 2 e 3.
# Como o Paulo está associado ao valor 1 e a Juliana ao valor 2,
# sobram mais dois possíveis valores para a Tamires poder ganhar ( 0 ou 3 ).