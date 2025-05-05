placas = []
multas = []

for i in range(15):
    placa = input(f"Digite a placa do carro {i+1}: ")
    multa = float(input(f"Digite o valor da multa do carro {i+1}: R$"))
    
    placas.append(placa)
    multas.append(multa)

medmultas = sum(multas) / len(multas)


maior = sum(1 for multa in multas if multa >= 300)

print(f"Média das multas: R${medmultas:.2f}")
print(f"Quantidade de carros com multa maior ou igual a R$300,00: {maior}")
