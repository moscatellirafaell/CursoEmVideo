prod = 'Caderno', 8.5,\
       'Lápis', 2,\
       'Caneta', 2.5,\
       'Borracha', 3.5,\
       'Régua', 3.7
print('-'*37)
print(f'{"LISTAGEM DE PREÇOS":^36}')
print('-'*37)
for p in range(0, len(prod)):
    if p % 2 == 0:
        print(f'{prod[p]:.<30}', end='')
    else:
        print(f'R${prod[p]:>5.2f}')
print('-'*37)
