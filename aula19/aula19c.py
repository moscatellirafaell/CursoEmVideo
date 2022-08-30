estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('UF: '))
    estado['SIGLA'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print()
for e in brasil:
    for k, v in e.items():
        print(f'{k}: {v}')
    print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
