soma=0
cont=0
nota=[0.0]*5
tamanho = len(nota)
for x in range (tamanho):
 nota[x]=float(input("nota: "))
#preenche o arnays
for i in range(tamanho):
 soma += nota[i]

media= soma/tamanho
for y in range (tamanho):
    if nota[y]>media:
     cont= cont+1
print(f"a média da sala é {media} e {cont} alunos tem notas acima da média")