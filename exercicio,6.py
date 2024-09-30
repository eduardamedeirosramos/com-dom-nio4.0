A=[0]*10
M=[0]*10
tamanho = len(A)
for y in range (tamanho):
    A[y]= int(input("insira o número: "))

x= int(input("insira o multiplicador: "))
for i in range(tamanho):
   M[i] = A[i] * x
   print(A)
   print(x)
   print(M)
#