# 3 - Modifique o programa anterior para que o usuário determine qual o intervalo da contagem.


intervalo_inferior = int(input("Digite o limite inferior: "))
intervalo_superior = int(input("Digite o limite superior: "))

contador = intervalo_inferior
while contador <= intervalo_superior:
    if contador % 2 != 0:  
        print(contador)
    contador += 1
