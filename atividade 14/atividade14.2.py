'''
2. Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0 à 25], [26 à 50], [51 à 75] e [76 à 100]. 
     A entrada de dados deve terminar quando for lido um número negativo.
'''

quantidade = True

while quantidade:
     print("Caso você queira parar o programa, digite um número negativo. ")
     numero = int(input("Digite um número: "))
     if numero >= 0 and numero <= 25:
          print("Seu número está entre [0 e 25]\n")     
     elif numero >= 26 and numero <= 50:
          print("Seu número está entre [26 e 50]\n")
     elif numero >= 26 and numero <= 50:
          print("Seu número está entre [26 e 50]\n")
     elif numero >= 51 and numero <= 75:
         print("Seu número está entre [51 e 75]\n")
     elif numero >= 76 and numero <= 100:
         print("Seu número está entre [76 e 100]\n")
     elif numero > 100:
          print("Digite um número menor que ou igual à 100\n")
     elif numero < 0 :
          print("Programa parado.")
          quantidade = False