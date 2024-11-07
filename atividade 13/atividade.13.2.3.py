#2. Faça um programa que verifique a senha e o login de um sistema e só finalize quando ele acertar os dados.  Considere: login = "tds01" | senha = "123"

# while True:
#     login = input("Qual o seu login? ")
#     senha = (input("Qual a sua senha? "))
#     if login != "tds01" or senha != 123:
#         print("Tente novamente! ")

#     elif login == "tds01" and senha == 123:
#         print("Login e senha corretos! ")
#     break



login_correto = "tds01"
senha_correta = "123"
max_tentativas = 3 

tentativas = 0
acesso_permitido = False  

while tentativas < max_tentativas and not acesso_permitido:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == login_correto and senha == senha_correta:
        acesso_permitido = True  
        print("Acesso permitido!")
    else:
        tentativas += 1
        print("Login ou senha incorretos. Tente novamente.")
        if tentativas < max_tentativas:
            print(f"Tentativas restantes: {max_tentativas - tentativas}")
        else:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")



