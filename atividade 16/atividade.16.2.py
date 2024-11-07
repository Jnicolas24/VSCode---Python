# 2 - Faça um Programa que peça as quatro notas de 3 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

aluno1 = []
aluno2 = []
aluno3 = []
alunos_media = 0

continuar = True

while continuar:
    for nota1 in range(4):
        nota = float(input("Digite as notas do primeiro aluno: "))
        aluno1.append(nota)
    print()
    for nota2 in range(4):
        nota = float(input("Digite as notas do segundo aluno: "))
        aluno2.append(nota)
    print()
    for nota3 in range(4):
        nota = float(input("Digite as notas do terceiro aluno: "))
        aluno3.append(nota)
    print()

    continuar = False

print(aluno1)
print(aluno2)
print(aluno3)

media1 = sum(aluno1) / 4
media2 = sum(aluno2) / 4
media3 = sum(aluno3) / 4

print() 

if media1 >= 7:
    alunos_media += 1
if media2 >= 7:
    alunos_media += 1
if media3 >= 7:
    alunos_media += 1

print(f"O total de alunos que tiveram uma média maior ou igual a 7 foram: {alunos_media}")
 

