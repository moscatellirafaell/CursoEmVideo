o = 's'
q = s = ma = me = 0
while o == 's':
    n = int(input('\nDigite um número: '))
    o = str(input('Quer digitar outro valor? [s/n]: ')).lower().strip()[0]
    q += 1
    s += n
    if q == 1:
        me = n
    if n > ma:
        ma = n
    if n < me:
        me = n
m = s / q
print('\nMédia: {:.1f}'.format(m))
print('Maior: {}'.format(ma))
print('Menor: {}'.format(me))
