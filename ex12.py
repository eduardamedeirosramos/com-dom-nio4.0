negativo=0
for y in range(10):
  num=int(input("digite o número: "))
  if num<0:
      negativo=negativo+1
print(f"encontramos {negativo} números negativos")