print("------------")
print("Atividade 12")
print("------------")

# Um desenvolvedor Python está tendo que adaptar um sistema americano de cadastro de clientes americanos
# para os clientes brasileiros. Ele está esbarrando em um problema,
# pois lá as pessoas têm o costume de se referir pelo sobrenome antes do primeiro nome, por exemplo: Smith, John .
#
# Ele deseja adaptar as mensagens do sistema para o padrão brasileiro, mas sem alterar a
# estrutura de dados que ele recebe do banco de dados.
#
# Digamos que ele queira exibir a seguinte mensagem: "Ola Sr. Leonardo Cordeiro", como ele
# pode formatar a string para obter o resultado desejado?

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))