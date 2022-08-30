print('\n10 termos de uma PA')
pt = int(input('\nprimeiro termo: '))
r = int(input('razão: '))
for c in range(pt, (pt+(10-1)*r)+r, r):
    print(c, end=' > ')
print('fim')
