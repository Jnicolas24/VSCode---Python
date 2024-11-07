 #Condicionais if-elif-else
'''
No python, quando temos condições para realizarmos ações, usamos o if-elif-else
 SE          |  if  |
------------------------
 SENAO SE          |  elif  |
------------------------
 SENAO          |  else  |
------------------------

sintaxe :
if *condicao* :
    *acao*
------------------
elif *condicao* : 
    *acao*
------------------
else :
    *acao*

****OBS: O python é uma linguagem de **IDENTIFICAÇÃO OBRIGATÓRIA**, onde é possivel demarcar
        cada bloco com base no recuo da linha
'''

print ("1 - Aluno")
print ("2 - Funcionário")
print("3 - Visitante")
tipoAcesso = input("Selecione uma opção: ")

if tipoAcesso == "1" or tipoAcesso == "2":
    print ("Acesso liberado")
elif tipoAcesso == "3":
    print("Faça um cadastro pra entrar!")
else :
    print("Acesso Negado!")