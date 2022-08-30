num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]? ')).strip().lower()
    if resp in 'n':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('=-'*30)
print(f'Lista completa: {num}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
