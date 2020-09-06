login = input("Digite o seu login:")
senha = input("Digite sua senha: ")
if login == "userpy01" and senha == "teste01":
    print("Bem-vindo userpy01")
elif login == "userpy02" and senha == "teste02":
    print("Bem-vindo userpy02")
elif login == "userpy03" and senha == "teste03":
    print("Bem-vindo userpy03")
elif login == "userpy04" and senha == "teste04":
    print("Bem-vindo userpy04")
else:
    print("Login falhou!")

#>>> list(range(10)) #Gera uma sequência de 0 à 9.
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#>>> list(range(1)11) #Gera uma sequência de 1 à 11.
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#>>> list(range(0,30,5)) #Gera uma sequência de 0 à 30 com step = 5.
#[0, 5, 10, 15, 20, 25]
#>>> list(range(0,-10,-1)) #Gera uma sequência numérica negativa.
#[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
#>>> list(range(0)) )) #Gera uma lista vazia.

contagem = 0
for contagem in range(1,10):
         print(contagem)

contagem = 0
while(contagem < 10):
         print(contagem)
         contagem = contagem + 1
