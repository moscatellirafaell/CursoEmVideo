n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[30m', end=' ')
        t += 1
    else:
        print('\033[m', end=' ')
    print(c, end='')
print('\n\033[mO número {} foi divisível \033[30m{}\033[m vezes'.format(n, t))
if t == 2:
    print('Logo, É um número primo')
else:
    print('Logo, NÃO é um número primo')
