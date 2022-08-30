times = 'PAL', 'COR', 'FLU', 'CAP', 'FLA', 'INT', 'ATL', 'RBB', 'SAN', 'SAO'
print(f'\n10 primeiros colocados no rasileirão Série A:\n{times}')
print(f'\n5 primeiros colocados no Brasileirão Série A:\n{times[0:5]}')
print(f'\nOs últimos 3 colocados:\n{times[-3:]}')
print(f'\nTimes em ordem alfabética:\n{sorted(times)}')
print(f'\nEm qual posição está o Internacional:\n{times.index("INT")+1}º colocado')
'''for c, col in enumerate(times):
    if col == 'INT':
        print(f'\nEm qual posição está o Internacional:\n{c+1}º colocado')'''
