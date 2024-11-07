'''
4. Faça um programa que simule a urna eletrônica. A tela a ser apresentada deverá ser da seguinte forma: 
As opções são:

1. Candidato Jair Rodrigues 
2. Candidato Carlos Luz 
3. Candidato Neves Rocha 
4. Nulo 
5. Branco  

O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes informações: 
a) O número de votos de cada candidato;
b) A porcentagem de votos nulos; 
c) A porcentagem de votos brancos; 
d) O candidato vencedor.
'''

votojair = 0
votocarlos = 0
votoneves = 0
nulo = 0
branco = 0


print("Urna Eletrônica\n")
print("Abaixo você tem os candidatos:")
print("1) - Candidato Jair Rodrigues")
print("2) - Candidato Carlos Luz")
print("3) - Candidato Neves Rocha")
print("4) - Branco")
print("5) - Nulo")
print("6) - Ver resultados\n")


continuar = True

while continuar:
    candidatos = int(input("Qual candidato você deseja votar? "))

    if candidatos == 1:
        print("Você votou em Jair Rodrigues\n")
        votojair += 1

    elif candidatos == 2:
        print("Você votou em Carlos Luz\n")
        votocarlos += 1

    elif candidatos == 3:
        print("Você votou em Neves Rocha\n")
        votoneves += 1

    elif candidatos == 4:
        print("Você optou pelo voto Nulo\n")
        nulo += 1

    elif candidatos == 5:
        print("Você optou pelo voto em Branco\n")
        branco += 1

    elif candidatos == 6:
        print("RESULTADO DA VOTAÇÃO")
        total_votos = votojair + votocarlos + votoneves + nulo + branco
        perc_nulos = (nulo / total_votos * 100) if total_votos > 0 else 0
        perc_branco = (branco / total_votos * 100) if total_votos > 0 else 0

        print(f"Candidato Jair Rodrigues: {votojair} votos")
        print(f"Candidato Carlos Luz: {votocarlos} votos")
        print(f"Candidato Neves Rocha: {votoneves} votos")
        print(f"Votos nulos: {nulo} votos")
        print(f"Votos em branco: {branco} votos")
        print(f"Porcentagem de votos nulos: {perc_nulos:.2f}%")
        print(f"Porcentagem de votos em branco: {perc_branco:.2f}%")

        
        if votojair > votocarlos and votojair > votoneves:
            vencedor = "Jair Rodrigues"
        elif votocarlos > votojair and votocarlos > votoneves:
            vencedor = "Carlos Luz"
        elif votoneves > votojair and votoneves > votocarlos:
            vencedor = "Neves Rocha"
        else:
            vencedor = "Não houve um candidato vencedor, pois votos nulos/brancos foram os mais votados"
 
        print(f"Candidato vencedor: {vencedor}")
        continuar = False
    else:
        print(f"Opção de voto inválida: {candidatos}\n")

