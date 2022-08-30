def metade(n=0):
    r = n / 2
    return r


def dobro(n=0):
    r = n * 2
    return r


def aumentar(n=0, t=0):
    r = n + (n * t / 100)
    return r


def diminuir(n=0, t=0):
    r = n - (n * t / 100)
    return r


def moeda(n=0, m='R$'):
    return f'{m}{n:>.2f}'.replace('.', ',')
