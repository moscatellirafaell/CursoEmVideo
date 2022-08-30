print('\n10 termos de uma PA')
pt = int(input('\nprimeiro termo: '))
r = int(input('razão: '))
c = 0
pa = pt
while c < 10:
    c += 1
    print(pa, end=' ')
    pa += r
t = 1
tot = 0
while t != 0:
    t = int(input('\nMais quantos termos quer ver? '))
    tot += t
    for c in range(pa, pa+t):
        print(pa, end=' ')
        pa += r
print('\nTotal de termos mostrados: {}'.format(tot+10))
