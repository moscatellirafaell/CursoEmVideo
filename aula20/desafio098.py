from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        msg = f' Contando de {i} até {f} de {p} em {p} '
        print('-' * len(msg))
        print(msg)
        sleep(1)
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.3)
        print()
        print('-' * len(msg))
        sleep(1)
        print()
    elif i > f:
        msg = f' Contando de {i} até {f} de {p} em {p} '
        print('-' * len(msg))
        print(msg)
        sleep(1)
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(0.3)
        print()
        print('-' * len(msg))
        sleep(1)
        print()


cont(1, 10, 1)
cont(10, 0, 2)
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
print()
cont(ini, fim, pas)
