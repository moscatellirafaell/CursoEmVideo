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


def resumo(n=0, aum=10, red=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{red}% de redução: \t{diminuir(n, red, True)}')
    print('-' * 30)
