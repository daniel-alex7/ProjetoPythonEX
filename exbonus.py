numeros = []

while True:
    numero = float(input("Digite um número (ou 'sair' para terminar): "))
    numeros.append(numero)
    
    continuar = input("Deseja adicionar outro número? (s/n): ").strip().lower()
    if continuar != 's':
        break


soma = sum(numeros)
media = soma / len(numeros) if numeros else 0


acima_da_media = sum(1 for numero in numeros if numero > media)

print(f"Soma dos números: {soma:.2f}")
print(f"Média dos números: {media:.2f}")
print(f"Quantidade de números acima da média: {acima_da_media}")
