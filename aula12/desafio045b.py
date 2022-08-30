from random import randint
from time import sleep
print('=' * 12, '\nJOKENPO\n', end='' '=' * 12)
j = int(input('\nFaça sua jogada:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\n>>> '))
print('\nJO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(0.5)
i = ('PEDRA', 'PAPEL', 'TESOURA')
c = randint(0, 2)
if c == 0:
    if j == 0:
        print('\nEMPATE!')
    elif j == 1:
        print('\nVOCÊ VENCEU!')
    elif j == 2:
        print('\nVOCÊ PERDEU!')
elif c == 1:
    if j == 0:
        print('\nVOCÊ PERDEU!')
    elif j == 1:
        print('\nEMPATE!')
    elif j == 2:
        print('\nVOCÊ VENCEU!')
elif c == 2:
    if j == 0:
        print('\nVOCÊ VENCEU!')
    elif j == 1:
        print('\nVOCÊ PERDEU!')
    elif j == 2:
        print('\nEMPATE!')
sleep(0.5)
print('\nVocê escolheu {}'.format(i[j]), '\nO computador escolheu {}'.format(i[c]))
