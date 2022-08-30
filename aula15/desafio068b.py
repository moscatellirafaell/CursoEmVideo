from random import randint
jkp = ('PEDRA', 'PAPEL', 'TESOURA')
print('-'*13)
print('JOKENPO')
print('-'*13)
win = True
v = 0
while win:
    pc = randint(1, 3)
    j = int(input('[1] PEDRA\n[2] PAPEL\n[3] TESOURA\n>>> '))
    if j == 1:#jogador pedra
        print(f'\nVocê escolheu {jkp[j-1]}')
        if pc == 1:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('empate...\n')
        elif pc == 2:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('VOCÊ PERDEU!\n')
            win = False
        elif pc == 3:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('VOCÊ GANHOU!\n')
            v += 1
    elif j == 2:#jogador papel
        print(f'Você escolheu {jkp[j-1]}')
        if pc == 1:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('VOCÊ GANHOU!\n')
            v += 1
        elif pc == 2:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('empate...\n')
        elif pc == 3:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('VOCE PERDEU!\n')
            win = False
    elif j == 3:#jogador tesoura
        print(f'Você escolheu {jkp[j-1]}')
        if pc == 1:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('VOCÊ PERDEU!\n')
            win = False
        elif pc == 2:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('VOCÊ GANHOU\n')
            v += 1
        elif pc == 3:
            print(f'O computador escolheu {jkp[pc-1]}')
            print('empate...!\n')
if v == 1:
    print('Você ganhou apenas uma vez...')
elif v == 0:
    print('Você não conseguiu ganhar nenhuma vez... Que azar!')
else:
    print(f'Você ganhou {v} vezes consecutivas!')
