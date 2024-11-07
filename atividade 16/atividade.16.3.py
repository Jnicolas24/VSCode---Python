#3 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.


consoantes = []

for vetor in range(10):
    maiuscula = str(input("Digite uma letra: "))
    maiuscula = maiuscula.upper()
    if maiuscula != "A" and maiuscula != "E" and maiuscula != "I" and maiuscula != "O" and maiuscula != "U":
        consoantes.append(maiuscula)
print(f"As consoantes digitadas são: {consoantes}")


