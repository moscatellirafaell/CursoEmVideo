from random import randint
pc = randint(1, 10)
j = 0
t = 1
while j != pc:
    j = int(input('Tente advinhar em qual número eu estou pensando (entre 1 e 10): '))
    if j < pc:
        print('Mais...')
    else:
        print('Menos...')
    if j != pc:
        t += 1
if t == 1:
    print('Você acertou de primeira! Eu estava realmente pensando no número {}'.format(pc))
else:
    print('Você tentou {} vezes até acertar que eu estava pensando no número {}'.format(t, pc))
