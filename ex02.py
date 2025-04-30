num = input("Digite um número: ")

invSTR = num[::-1]

inv = int(invSTR)
num2 = int(num)

soma = inv + num2

print(f"O inverso de {num} é {invSTR}") 

print(f"A soma é {soma}")