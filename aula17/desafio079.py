num = []
c = 0
while True:
    n = int(input('\nDigite um número: '))
    if n not in num:
        num.append(n)
        print('Número adicionado')
    else:
        print('Número duplicado')
    o = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    if o == 'n':
        break
    while 's' not in o:
        o = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
print(f'\nNúmeros adicionados em ordem crescente: {sorted(num)}')
