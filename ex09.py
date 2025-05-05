
dias = []
chuva = []

for i in range(10):
    dia = input(f"Digite o dia da semana {i+1}: ")
    volchuva = float(input(f"Digite o volume de chuva para o dia {i+1}: "))
    
    dias.append(dia)
    chuva.append(volchuva)


chuvaqua = [chuva[i] for i in range(10) if dias[i].lower() == "quarta-feira"]

mediaqua = sum(chuva_quarta) / len(chuvaqua) if chuvaqua else 0


soma_chuva = sum(chuva)

print(f"Média de chuva na quarta-feira: {media_chuva_quarta:.2f} mm")
print(f"Soma total do volume de chuva: {soma_chuva:.2f} mm")
