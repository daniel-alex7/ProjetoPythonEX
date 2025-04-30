texto = input("Entre com uma string: ").upper()

contador = {}

for caractere in texto:
    if caractere in contador:
        contador[caractere] += 1
    else:
        contador[caractere] = 1


for caractere, quantidade in contador.items():
    print(f"O caractere {caractere} aparece {quantidade} vez")



