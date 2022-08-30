matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = stc = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'valor para posição [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
    print()
'''for c in range(0, 3):
    for v in matriz[c]:
        if v % 2 == 0:
            sp += v'''
for v in matriz:
    stc += v[2]
for v in matriz[1]:
    if v > mai:
        mai = v
print('-='*30)
print(f'soma dos valores pares: {sp}')
print(f'soma dos valores da terceira coluna: {stc}')
print(f'maior valor da segunda linha: {mai}')
print()
