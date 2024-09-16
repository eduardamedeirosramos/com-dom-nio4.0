n1= float(input ("digite a primeira nota: "))
while n1<0 or n1>10:
    n1 = float(input("tente novamente: "))
n2 = float(input("digite a segunda nota: "))
while n2<0 or n2>10:
    n2 = float(input ("tente novamente: "))
media = (n1+n2)/2
print(media)