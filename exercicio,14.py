def contarvogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

texto = "O RATO ROEU A ROUPA DO REI DE ROMA"
resultado = contarvogais(texto)
print(resultado)
