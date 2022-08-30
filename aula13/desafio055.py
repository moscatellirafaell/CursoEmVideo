ma = 0
me = 0
for c in range(1, 6):
    p = float(input('Peso da {}ª pessoa (kg): '.format(c)))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('\nMaior peso: {}kg\nMenor peso: {}kg'.format(ma, me))
