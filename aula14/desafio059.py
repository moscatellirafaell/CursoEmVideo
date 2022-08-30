o = 0
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
s = v1 + v2
m = v1 * v2
ma = v1
if v2 > v1:
    ma = v2
while o != 5:
    print('\nEscolha uma opção')
    o = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n>>> '))
    if o == 1:
        print('\nValor da soma entre {} e {}: {}'.format(v1, v2, s))
    elif o == 2:
        print('\nValor da multiplicação entre {} e {}: {}'.format(v1, v2, m))
    elif o == 3:
        if v1 == v2:
            print('\nOs dois valores são iguais')
        else:
            print('\nMaior valor entre {} e {}: {}'.format(v1, v2, ma))
    elif o == 4:
        v1 = int(input('\nDigite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))
        s = v1 + v2
        m = v1 * v2
        ma = v1
        if v2 > v1:
            ma = v2
    elif o == 5:
        print('Encerrando...')
    else:
        print('\nOPÇÃO INVÁLIDA')
