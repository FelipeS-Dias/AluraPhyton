print("------------")
print("Atividade 11")
print("------------")

for i in range(1,8):
    if(i == 5):
        continue
    print(i)

# O Exercicio era para identificar qual seria o resultado impresso sem realizar a execução do código.
# Pula apenas a iteração 5. A saída será:
#
# 1
# 2
# 3
# 4
# 6
# 7

# O continue não sai do laço, apenas pula a iteração.