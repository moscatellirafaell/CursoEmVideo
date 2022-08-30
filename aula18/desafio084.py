pessoas = list()
dados = list()
pesados = list()
leves = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    o = input('Quer continuar [S/N]? ').lower().strip()
    if o == 'n':
        break
    while o not in 's':
        o = input('Quer continuar [S/N]? ').lower().strip()
for p in pessoas:
    if p[1] == mai:
        pesados.append(p[0])
    elif p[1] == men:
        leves.append(p[0])
print()
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print(f'Maior peso foi de {mai}kg. Peso de {pesados}')
print(f'Menor peso foi de {men}kg. Peso de {leves}')
print()
