print("------------")
print("Atividade 10")
print("------------")

i = 1

while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break

# O Exercicio era para identificar qual seria o resultado impresso sem realizar a execução do código.
# print = 1, 2, 3 e 4
# Isso porque a condição if, que executa o break (que rompe o laço da iteração),
# é executada após o incremento da variável i, sendo assim, quando o valor dela for 5,
# a repetição para antes que o programa tenha chance de imprimir o valor 5.