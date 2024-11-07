#1- Escreva um programa que mostre os números de 1 até 100.

#Aqui, uma variável chamada contador é inicializada com o valor 0. Essa variável servirá para contar de 0 até 100.
contador = 0

'''
Este é um loop while, que continuará executando o bloco de código dentro dele enquanto a condição contador <= 100 for verdadeira. 
Ou seja, enquanto o valor de contador for menor ou igual a 100.
'''
while contador <= 100:

#Dentro do loop, a função print exibe o valor atual de contador na tela.
    print(contador)

#Essa linha aumenta o valor de contador em 1 a cada iteração do loop. O operador += é uma forma abreviada de escrever contador = contador + 1.    
    contador += 1