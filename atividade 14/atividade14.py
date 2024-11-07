'''
1. Escrever um algoritmo que lê 5 valores, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.
'''



#Aqui, você inicializa a variável núm_negativos com 0, que irá contar quantos valores negativos foram digitados.
# núm_negativos = 0


#Você lê o primeiro valor (v1) como um número de ponto flutuante. Se v1 for menor que 0, incrementa núm_negativos em 1.
# v1 = float(input("Digite o primeiro valor: "))
# if v1 < 0:
#     núm_negativos += 1

# #O mesmo comentário acima, serve para os quatro valores valores em seguida.
# v2 = float(input("Digite o segundo valor: "))
# if v2 < 0:
#     núm_negativos += 1

# v3 = float(input("Digite o terceiro valor: "))
# if v3 < 0:
#     núm_negativos += 1

# v4 = float(input("Digite o quarto valor: "))
# if v4 < 0:
#     núm_negativos += 1

# v5 = float(input("Digite o quinto valor: "))
# if v5 < 0:
#     núm_negativos += 1

#     #Para cada valor, você lê o número e verifica se é negativo, incrementando núm_negativos conforme necessário.


# #Você imprime a contagem total de valores negativos
# print("Total de valores negativos: ", núm_negativos)

valor = 1
num_negativo = 0

while valor <= 5:
    num = int(input("Digite um número: \n"))
    valor += 1
    if num < 0:
        num_negativo += 1
    elif num == 0:
        print(f"O número {num} é neutro! \n")
        
print(f"Você teve {num_negativo} números negativos no seu código! \n")














