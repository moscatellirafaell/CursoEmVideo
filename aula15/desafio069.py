mais18 = mtot = m20menos = 0
while True:
    i = int(input('\nIdade: '))
    if i > 18:
        mais18 += 1
    s = ' '
    while s not in 'mf':
        s = str(input('Sexo [M/F]: ')).lower().strip()[0]
    if s == 'm':
        mtot += 1
    if s == 'f' and i < 20:
        m20menos += 1
    o = ' '
    while o not in 'sn':
        o = str(input('Continuar [S/N]? ')).lower().strip()[0]
    if o == 'n':
        break
print(f'\nTotal de pessoas com mais de 18 anos: {mais18}')
print(f'Total de homens: {mtot}')
print(f'Total de mulheres com menos de 20 anos: {m20menos}')
