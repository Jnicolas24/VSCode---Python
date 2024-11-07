#Variáveis e tipos

'''
Para criar variaveis no python, basta digitar o nome do identificador
e usar o símbolo de igualdade (=) para fazer a atribuição, após isso
é só colocar o valor que deseja armazenar.

Em python, as variaveis são dinamicamente tipadas, ou seja, não precisamos
dizer o tipo dela quando a criamos, o que determina essa tipagem é o que
irá ser atríbuido. Sendo assim, uma variável pode guardar um texto (str)
e depois guardar um número inteiro (int) por exemplo.
'''

#variavel do tipo caractere ---> string (str)
produto = "Banana" #a string pode ser atribuida guardando usando aspas simples('') ou dupla("")

#variavel do tipo real ---> float
valor = 4.3 #p/ números do tipo flutuante(float), usamos o ponto(.) para separar as casas decimais

#variavel do tipo inteiro --> integer (int)
quantidade = 12 #p/ o tipo inteiro (int), basta escrever o valor sem as aspas

#variavel do tipo logica --> boolean (bool)
temEstoque = True #variaveis do tipo logico (bool) sempre guardam os valores True ou False


#para saber o tipo de uma variável usamos a função type(), dentro dos parenteses
#a variavel que deseja
type(produto)
#print ("Tipo de variavel produto ", type(produto))
#print ("Tipo de variavel valor ", type(valor))
#print ("Tipo de variavel quantidade ", type(quantidade))
#print ("Tipo de variavel temEstoque ", type(temEstoque))

#-----------------------------------------------------------------------------------------------------------------------------------------

#Operadores aritméticos

'''
Soma          |  +  |
------------------------
Subtração     | - |
------------------------
Multiplicação  | * |
------------------------
Divisão       | / |
------------------------
Divisão truncada(inteira)  |  // |
------------------------------------
Potência      | ** |
----------------------
Módulo        | % |
------------------------------------
'''

#por default (padrão), todo input é uma string

#int() transforma o valor para inteiro
n1 = int(input("Digite um número: "))

#float() transforma o valor para real
n2 = input("Digite outro número: ")
n2 = float(n2) 

#o mais (+) pode ser usado para somar (quando usado para numeros)
#e para concatenar (quando usados em strings)
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divTrun = n1 // n2
mod = n1 % n2
pot = n1 ** n2

# print ("Soma: ", n1, " + ", n2, "=", soma) #forma concatenada
# print(f"Subtração: {n1} - {n2} = {sub}") #forma interpoada
# print(f"Multiplicação: {n1} x {n2} = {mult}")
# print(f"Divisão: {n1} / {n2} = {div}")
# print(f"Divisão Truncada: {n1} // {n2} = {divTrun}")
# print(f"Módulo: {n1} % {n2} = {mod}")
# print(f"Potência: {n1} ^ {n2} = {pot}")

#----------------------------------------------------------------------------

#Operadores Relacionais
'''
Igual              | == |
-------------------------
Diferente          | - |
-------------------------
Maior que          | > |
------------------------
Maior igual          | >= |
------------------------
Menor que          | < |
------------------------
Menor igual          | <= |
------------------------
'''

#Operadores Lógicos
'''
 E           | and |
------------------------
 OU          | or |
------------------------
  NÃO        | not |
------------------------
'''