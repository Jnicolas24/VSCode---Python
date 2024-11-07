#7 - Crie um programa que solicite ao usuário um número inteiro n e imprima um quadrado de asteriscos (*) de tamanho n x n. 

numero = int(input("Digite um número inteiro para o quadrado: \n"))

contador = 1
n = int(numero)

#Para coluna
while contador <= numero:
    contador += 1
    contador2 = 0

#Para linha
linha = 0
while linha < n:
    print(' * ' * n)
    linha += 1










