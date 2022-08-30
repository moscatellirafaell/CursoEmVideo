n = q = s = 0
while n < 999:
    n = int(input('Digite um número (999 para encerrar): '))
    if n < 999:
        q += 1
        s += n
print('\nQuantos números foram digitados: {}'.format(q))
print('Soma entre os números digitados: {}'.format(s))
