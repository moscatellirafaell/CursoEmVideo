from random import randint
v = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(0, 10)
    s = n + pc
    j = ' '
    while j not in 'pi':
        j = str(input('Par ou Ímpar [P/I]? ')).lower().strip()[0]
    print(f'Você jogou {n} e o computador jogou {pc}\nTotal: {s}')
    print('...Deu PAR' if s % 2 == 0 else '...Deu ÍMPAR')
    if j == 'p':
        if s % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif j == 'i':
        if s % 2 != 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
if v == 0:
    print('\nVocê não consegiu vencer nenhuma vez... Que azar!')
elif v == 1:
    print('\nVocê venceu apenas uma vez')
else:
    print(f'\nVocê venceu {v} vezes consecutivas!')
