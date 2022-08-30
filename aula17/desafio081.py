num = list()
while True:
    num.append(int(input('\nDigite um número: ')))
    o = str(input('Quer continuar [S/N]? ')).strip().lower()
    if o == 'n':
        break
    while o not in 's' or o == '':
        o = str(input('Quer continuar [S/N]? ')).strip().lower()
print(f'\nTotal de números digitados: {len(num)}')
num.sort(reverse=True)
print(f'Ordem decrescente dos números: {num}')
if 5 in num:
    print(f'O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')
