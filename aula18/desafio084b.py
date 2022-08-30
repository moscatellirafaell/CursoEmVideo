temp = []
prin = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prin.append(temp[:])
    temp.clear()
    r = str(input('Continuar? '))
    if r in 'Nn':
        break
print('-='*30)
print(f'total de pessoas: {len(prin)}')
print(f'maior peso: {mai}kg de ', end='')
for p in prin:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'menor peso: {men}kg de ', end='')
for p in prin:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
