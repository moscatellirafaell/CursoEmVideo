val = list()
for c in range(0, 5):
    val.append(int(input('Digite um valor: ')))
men = mai = 0
for cc, v in enumerate(val):
    if cc == 0:
        men = mai = v
    if v < men:
        men = v
    if v > mai:
        mai = v
print(f'\nMenor valor {men} na(s) posição(ões):', end=' ')
for cc, v in enumerate(val):
    if v == men:
        print(cc, end='... ')
print(f'\nMaior valor {mai} na(s) posição(ões):', end=' ')
for cc, v in enumerate(val):
    if v == mai:
        print(cc, end='... ')
print()
