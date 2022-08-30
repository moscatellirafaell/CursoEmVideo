def metade(n=0, form=False):
    r = n / 2
    return r if form is False else moeda(r)


def dobro(n=0, form=False):
    r = n * 2
    return r if form is False else moeda(r)


def aumentar(n=0, t=0, form=False):
    r = n + (n * t / 100)
    return r if not form else moeda(r)


def diminuir(n=0, t=0, form=False):
    r = n - (n * t / 100)
    return r if not form else moeda(r)


def moeda(n=0, m='R$'):
    return f'{m}{n:>.2f}'.replace('.', ',')
