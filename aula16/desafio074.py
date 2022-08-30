from random import randint
num = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'\nNúmeros gerados: {num}')
print(f'Menor número: {sorted(num)[:1]}')
print(f'Maior número: {sorted(num)[-1:]}')

print('-'*40)

print('Números gerados:', end=' ')
for n in num:
    print(n, end=' ')
print(f'\nMenor número: {min(num)}')
print(f'Maior número: {max(num)}')
