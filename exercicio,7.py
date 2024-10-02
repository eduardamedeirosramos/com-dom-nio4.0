num=[0]*5
tamanho=len(num)
for x in range(tamanho):
    num[x]= int(input("insira um número: "))
for i in range (4,-1,-1):
 print (num[i], end= " ")
