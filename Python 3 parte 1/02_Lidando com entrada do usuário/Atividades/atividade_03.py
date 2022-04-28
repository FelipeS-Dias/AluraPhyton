print("____________")
print("Atividade 03")
print("____________")

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if(idade > 18):
    print("Você é maior de idade.")
else:
    # if(idade < 12):
    #     print("Você é uma criança.")
    # elif(idade > 12):
    #     print("Você é um adolescente.")

    if (idade <= 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")

# O Exercicio era para identificar oque acontece quando o usuário digitar 12.

# Quando o usuário digitar 12, nenhuma condição será satisfeita, porque
# 12 não é maior que 18 (idade > 18).
# 12 não é menor que 12 (idade < 12).
# 12 não é maior que 12 (idade > 12).
#
# Para corrir é necessário definir se 12 vai corresponder a "Criança" ou "Adolescente"
# assim utilizando o operador correto ( <= ) ou ( >= ) respectivamente.
#
# Operadores de comparação:
#
# < - menor que
# > - maior que
# <= - menor ou igual a
# >= - maior ou igual a
# == - igual a
# != - diferente de