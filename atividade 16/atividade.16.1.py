# 1 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# lista com 5 números inteiros
vetor = [1, 2, 3, 4, 5]

# variáveis para soma e multiplicação
soma = 0
multiplicacao = 1

# Calculo da soma e da multiplicação
for result in vetor:
    soma += result          
    multiplicacao *= result

# Mostra os resultados
print("Números: ", vetor)
print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)

