grupo = []
pessoas = {}
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).lower()[0]
        if pessoas['sexo'] in 'mf':
            break
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    grupo.append(pessoas.copy())
    while True:
        op = str(input('Continuar [S/N]? ')).lower()[0]
        if op in 'sn':
            break
    if op == 'n':
        break
    print()
print()
print(f'Quantidade de pessoas no grupo: {len(grupo)}')
media = soma/len(grupo)
print(f'Média de idade do grupo: {media:.1f}')
print('Mulheres do grupo:', end=' ')
for p in grupo:
    if p['sexo'] == 'f':
        print(f'- {p["nome"]}', end='  ')
print()
print('Pessoas acima da média de idade:', end=' ')
for p in grupo:
    if p['idade'] > media:
        print(f'- {p["nome"]}', end='  ')
print()
