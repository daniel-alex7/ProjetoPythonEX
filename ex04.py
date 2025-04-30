text = input("Digite uma palavra: ")
invt =  text[::-1]

if text == invt:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")