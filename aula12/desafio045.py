import emoji
from time import sleep
from random import randint
print('\033[7m-\033[m' * 13)
print('\033[1;7m   JOKENPÔ   \033[m')
print('\033[7m-\033[m' * 13)
p = int(input('Escolha:\n[1] pedra\n[2] papel\n[3] tesoura\n>>> '))
c = randint(1, 3)
#player escolhe pedra
if p == 1 and c == 2:
    print(emoji.emojize('Você escolheu PEDRA :fist:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('PAPEL! :hand:', language='alias'))
    sleep(1)
    print('VOCÊ PERDEU!')
elif p == 1 and c == 3:
    print(emoji.emojize('Você escolheu PEDRA :fist:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('TESOURA! :v:', language='alias'))
    sleep(1)
    print('VOCÊ VENCEU!')
elif p == 1 and c == 1:
    print(emoji.emojize('Você escolheu PEDRA :fist:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('PEDRA! :fist:', language='alias'))
    sleep(1)
    print('EMPATE!')
#player escolhe papel
if p == 2 and c == 2:
    print(emoji.emojize('Você escolheu PAPEL :hand:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('PAPEL! :hand:', language='alias'))
    sleep(1)
    print('EMPATE!')
elif p == 2 and c == 3:
    print(emoji.emojize('Você escolheu PAPEL :hand:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('TESOURA! :v:', language='alias'))
    sleep(1)
    print('VOCÊ PERDEU!')
elif p == 2 and c == 1:
    print(emoji.emojize('Você escolheu PAPEL :hand:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('PEDRA! :fist:', language='alias'))
    sleep(1)
    print('VOCÊ VENCEU!')
#player escolhe tesoura
if p == 3 and c == 2:
    print(emoji.emojize('Você escolheu TESOURA :v:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('PAPEL! :hand:', language='alias'))
    sleep(1)
    print('VOCÊ VENCEU!')
elif p == 3 and c == 3:
    print(emoji.emojize('Você escolheu TESOURA :v:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('TESOURA! :v:', language='alias'))
    sleep(1)
    print('EMPATE!')
elif p == 3 and c == 1:
    print(emoji.emojize('Você escolheu TESOURA :v:', language='alias'))
    sleep(1)
    print('O computador escolheu...')
    sleep(2)
    print(emoji.emojize('PEDRA! :fist:', language='alias'))
    sleep(1)
    print('VOCÊ PERDEU!')
