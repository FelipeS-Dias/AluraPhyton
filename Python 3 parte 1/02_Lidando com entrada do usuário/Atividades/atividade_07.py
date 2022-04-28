print("____________")
print("Atividade 07")
print("____________")

dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

print("Em {} o Carnaval acontece em {} do dia {} até o dia {}" .format(ano, mes, dia_ini, dia_fim))

# Dentro da string, devemos utilizar as chaves ({}) para definir onde o valor da variável deve ser inserido.
# E logo após a definição da string, chamamos a função .format(),
# que recebe as variáveis/parâmetros na ordem de inserção
#
# Essa formatação, que também é chamada de interpolação.