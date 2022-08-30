num = list()
while True:
    num.append(int(input('\nDigite um número: ')))
    o = str(input('Quer continuar [S/N]? ')).strip().lower()
    if o == 'n':
        break
    while o not in 's' or o == '':
        o = str(input('Quer continuar [S/N]? ')).strip().lower()
print(f'\nNúmeros digitados: {num}')
print('Números pares:', end=' ')
for a, b in enumerate(num):
    if b % 2 == 0:
        print(b, end='... ')
print('\nNúmeros ímpares:', end=' ')
for a, b in enumerate(num):
    if b % 2 != 0:
        print(b, end='... ')
