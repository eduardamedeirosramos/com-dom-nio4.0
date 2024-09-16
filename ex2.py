G=5.80
E=4.90

combustivel= (input ("informe G para gasolina e etanol E"))
quantidade= float(input("quantidade: "))

if combustivel == "G" or combustivel == "g":
    print(f"valor a pagar R$ {quantidade*G:2f}galosina")
else:
    if combustivel == "E" or combustivel == "e":
        print(f"valor a pagar R$ {quantidade*E:2f} etanol")
    else:
        print("valor invalido")