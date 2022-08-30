num = [[], []]
for v in range(0, 7):
    val = int(input(f'{v+1}º valor: '))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)
print('-='*30)
print(f'valors pares digitados: {sorted(num[0])}')
print(f'valores ímpares digitados: {sorted(num[1])}')
print()
