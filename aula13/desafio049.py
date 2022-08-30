t = int(input('Escolha um número: '))
print('='*13)
print('TABUADA DO {}'.format(t))
print('='*13)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(t, c, t*c))
