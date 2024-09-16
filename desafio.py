pin = 2704
senha = int(input("digite sua senha: "))
tentativas = 1
while senha != pin and tentativas <3:
  senha = int(input(f"senha incorreta, tente novamente\n"
                   f"você tem {3-tentativas} tentativas:"))
  tentativas+=1
if tentativas == 3 and senha != pin:
 print("senha bloqueada")
else:
 print ("login efetuado com sucesso!")
