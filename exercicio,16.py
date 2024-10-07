nomes = [""]*5
tam= len(nomes)
for x in range (tam):
 nomes[x] = str(input("nome: "))
print(f"os nomes digitados foram: {nomes}")

for y in range (tam-1,-1,-1):
    print(nomes[y])