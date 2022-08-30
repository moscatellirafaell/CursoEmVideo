num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'\nNúmeros digitados: {num}')
print(f'O número 9 foi digitado {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número 3 foi digitado na posição {num.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
print('Números pares digitados:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end='  ')
