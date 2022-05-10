# import atividade_16_1
# import atividade_16_2
#
# print("--------------")
# print("Atividade 16.3")
# print("--------------")

# O Exercicio era para identificar qual seria o resultado impresso sem realizar a execução do código.

# Neste primeiro exemplo os arquivos(16.1 e 16.2) não possui uma função definida, assim que realiza o IMPORT
# eles já são executados antes de enviar a mensagem que possui no arquivo 16.3

# --------------
# Atividade 16.1
# --------------
# Executando A
# --------------
# Atividade 16.2
# --------------
# Executando B
# --------------
# Atividade 16.3
# --------------

# Já no código abaixo, tendo definido a função "def executa()" nos arquivos(16.1 e 16.2), ao executa-lo
# o resultado será primeiro a impressão das informações do arquivo(16.3) e após os outros.

import atividade_16_1
import atividade_16_2

print("--------------")
print("Atividade 16.3")
print("--------------")

print("Executei Primeiro")

atividade_16_1.executa()
atividade_16_2.executa()