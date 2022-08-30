s = 0
v = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        v += 1
print('\nSoma dos {} valores ímpares e múltiplos de três entre 1 e 500: {}'.format(v, s))
