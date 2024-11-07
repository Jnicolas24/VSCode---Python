#5 - Modifique o programa anterior para exibir qual deles é o menor número.

contador = 0

numero = int(input("Digite um número: "))
mnumero = numero

contador += 1

while contador < 3:
    numero = int(input("Digite um número: "))
    if numero < mnumero:
        mnumero = numero

    contador += 1


print("O seu menor número é:", mnumero)

