valor = []
par = []
impar = []

while True: 
    n = int(input('Digite um número inteiro e 0 para parar: '))

    if n == 0:
        break

    valor.append(n)

for n in valor:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    
print(f'\nÉ par? {par}')
print(f'É ímpar? {impar}')
print(f'Valores = {valor}')

        