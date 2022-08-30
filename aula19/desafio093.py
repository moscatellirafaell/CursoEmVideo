jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
print()
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'{k}: {v}')
print()
print(f'{jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'>>> Na partida {i}, fez {v} gols')
print(f'Total de {jogador["total"]} gols')
