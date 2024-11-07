'''
Laço for: usamos esse tipo de iteração quando sabemos quantas
vezes será necessárias o laço acontecer, ou seja, não dependemos
de uma condição como no while
'''

# lista_nomes = ["Ana", "João", "Antonia", "Marcio"]

# for nome in lista_nomes: #para cada nome na lista_nomes
#     print(nome) #exibe o nome



'''
1- Receba nomes do usuário até que o usuário digite 0, depois exiba
quais desses nomes iniciam com a letra A.
'''


lista_nomes = [] #cria uma lista vazia
n = input("Digite um nome: ") #solicita um nome ao usuário

while n != '0': #enquanto o nome digitado for diferente de 0
    lista_nomes.append(n) #adiciona o nome digitado na lista
    print (lista_nomes) #exibe a nova lista
    n = input("Digite um nome: ") #pede outro nome

print("Lista final", lista_nomes) #Mostra a lista final 

for nome in lista_nomes:
    nome = nome.upper()
    if nome.startswith('A'):
        print(nome)


'''
2 - Faça um programa que receba 10 números e ao final, exiba o
dobro do valor digitado, se esse numero foi maior que 8.
'''

# lista_valores = []

# for n in range(10):
#     v = int(input("Digite um número: "))
#     if v > 8:
#         lista_valores.append(v*2)
#     else:
#         lista_valores.append(v)
#     print(lista_valores)

# print(range(10)) #a função range cria um intervalo
# print(list(range(10)))

# print("#"*10)

# print(range(2, 10)) #determinando o inicio e o fim do intervalo
# print(list(range(2,10)))

# print ("#"*10)

# #determinando o inicio e o fim do intervalo e o passo
# print(range(1, 11, 2))
# print (list(range(1, 11, 2))) 
