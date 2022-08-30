print('\n10 termos de uma PA')
pt = int(input('\nprimeiro termo: '))
r = int(input('razão: '))
c = 0
pa = pt
while c < 10:
    c += 1
    print(pa, end=' ')
    pa += r
