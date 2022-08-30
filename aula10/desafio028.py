'''import random
player = int(input('Tente advinhar em qual número eu estou pensando (entre 0 e 5): '))
lista = [0, 1, 2, 3, 4, 5]
num = random.choice(lista)
if player == num:
    print('\033[1;32mVocê acertou!\033[m Eu estava pensando no \033[4mnúmero {}\033[m'.format(num))
else:
    print('\033[1;31mVocê errou!\033[m Eu estava pensando no \033[4mnúmero {}\033[m'.format(num))'''

from random import randint
from time import sleep
n = randint(0, 5)
p = int(input('Tente advinhar em qual número eu estou pensando (entre 0 e 5): '))
print('\033[3mprocessando...\033[m')
sleep(1.5)
if p == n:
    print('\033[1;32mVocê acertou!\033[m Eu estava pensando no \033[4mnúmero {}\033[m'.format(n))
else:
    print('\033[1;31mVocê errou!\033[m Eu estava pensando no \033[4mnúmero {}\033[m'.format(n))
