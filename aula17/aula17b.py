val = list()
for cont in range(0, 5):
    val.append(int(input('Digite um valor: ')))

for c, v in enumerate(val):
    print(f'Valor {v} na posição {c}')
