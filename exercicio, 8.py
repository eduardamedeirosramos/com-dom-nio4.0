nome = [" "]*3
senha= [" "]*3
tam= len (nome)

for x in range (tam):
 nome[x]= input("insira seu nome: ")
 senha[x] = input(f"insira sua senha,{nome [x]}: ")

for i in range (tam):
    print(f" {i} - nome:{nome[i]}, senha:{senha[i]}")