# 6 - Adicione ao programa anterior a exibição do maior número digitado.

contador = 0

numero = int(input("Digite um número: "))
menor_numero = numero
maior_numero = numero

contador += 1

while contador < 3:
    numero = int(input("Digite um número: "))
    if numero < menor_numero:
        menor_numero = numero
    
    elif numero > maior_numero:
        maior_numero = numero

    contador += 1


print("O seu menor número é:", menor_numero)

print("Seu maior número é:", maior_numero)
