cont=0
contfora=0
for y in range(10):
 num=int(input("digite um número: "))
 if num>=10 and num<=20:
  cont=cont+1
 else:
    contfora=contfora+1
print(f"dentro do intervalo temos {cont} fora do intervalo temos {contfora}")
