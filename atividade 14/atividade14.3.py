'''
3. Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10. 
     De maneira que sejam impressos somente as multiplicações cujo resultado seja um número par.
'''

numero = int(input("Digite seu número: "))

tabuada = 1

#Este loop continuará enquanto a tabuada for < ou = a 10
while tabuada <= 10:

#Esta linha aumenta o valor de tabuada em 1 a cada iteração do loop. Isso garante que o loop prossiga para a próxima multiplicação até atingir 10.
    tabuada += 1

#Calcula o resultado da multiplicação entre o número fornecido pelo usuário e o valor atual de tabuada
    result = numero * tabuada


#Este if verifica se o resultado da multiplicação é par. O operador % (módulo) retorna o resto da divisão de result por 2. Se o resto for 0, significa que o número é par.
    if result % 2 == 0:


#Se o resultado for par, esta linha imprime o cálculo da multiplicação em um formato legível, usando uma f-string para inserir as variáveis diretamente na string.
        print(f"{numero} x {tabuada} = {result}")


