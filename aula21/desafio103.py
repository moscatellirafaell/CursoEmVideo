def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


nome = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)
