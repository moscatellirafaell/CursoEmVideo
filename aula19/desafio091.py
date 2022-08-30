from random import randint
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
#ranking = []
for k, v in jogo.items():
    print(f'{k}: {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
