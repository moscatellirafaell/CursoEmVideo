jogador = {}
jogadores = []
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        op = str(input('Continuar [S/N]? ')).lower()[0]
        if op in 'sn':
            break
    if op == 'n':
        break
    print()
print()
print(f'{"Nº "}{"Nome":<15}{"Gols":<15}{"Total":<15}')
for n, j in enumerate(jogadores):
    print(f'{n:<2} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    op2 = int(input('Mostrar dados de qual jogador (999 ENCERRA)? '))
    if op2 == 999:
        break
    if op2 >= len(jogadores):
        print('Jogador não encontrado')
    else:
        print(f'Jogador {jogadores[op2]["nome"]}:')
        for i, g in enumerate(jogadores[op2]['gols']):
            print(f'- No jogo {i+1} fez {g} gols')
    print()
