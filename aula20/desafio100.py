from random import randint
from time import sleep


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    for n in numeros:
        print(n, end=' ')
        sleep(0.3)
    print()


def somaPar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'Soma dos pares: {s}')


numeros = []
sorteia()
somaPar()
