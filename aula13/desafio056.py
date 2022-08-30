itot = 0
hv = 0
nhv = ''
m20 = 0
for c in range(1, 5):
    print('\n{}ª pessoa'.format(c))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [m/f]: ')).strip().lower()
    itot += i
    if s == 'm' and i > hv:
        hv = i
        nhv = n
    elif s == 'f' and i < 20:
        m20 += 1
m = itot/4
print('\nIdade média do grupo: {:.1f}'.format(m))
print('O homem mais velho tem {} anos e se chama {}'.format(hv, nhv))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(m20))
