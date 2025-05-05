salarios = []

for i in range(10):
    salario = float(input(f"Digite o salário do trabalhador {i+1}: R$"))
    salarios.append(salario)

media_salarios = sum(salarios) / len(salarios)


maior_salario = max(salarios)

salmenor = sum(1 for salario in salarios if salario < 850)

print(f"Média dos salários: R${media_salarios:.2f}")
print(f"Maior salário: R${maior_salario:.2f}")
print(f"Quantidade de salários menores que R$850,00: {salmenor}")
