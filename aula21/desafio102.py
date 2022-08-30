def fatorial(num=0, show=False):
    """
    -> calcula o fatorial de um numero
    :param num: O numero a ser calculado
    :param show: (opcional) mostrar o calculo ou ao
    :return: fatorial de um num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c == 1:
                print(f'{c} =', end=' ')
            else:
                print(f'{c} x', end=' ')
        f *= c
    return f


print(fatorial(5))
# help(fatorial)
