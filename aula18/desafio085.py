val = list()
par = list()
impar = list()
for v in range(0, 7):
    val.append(int(input(f'{v+1}º valor: ')))
for v in val:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print()
print(f'Valores pares: {sorted(par)}')
print(f'Valores ímpares: {sorted(impar)}')
print()
