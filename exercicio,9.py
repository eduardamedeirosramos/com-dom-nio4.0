cont=0
num = [0]*10
for x in range(len(num)):
    num[x] =  int(input("digite um número:"))
    j =  int(input("informe a pesquisa: "))
for i in range(len(num)):
    if j == num[i]:
        cont+=1
print(cont)