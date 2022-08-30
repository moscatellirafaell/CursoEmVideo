f = str(input('Escreva uma frase: ')).replace(' ', '').upper()
inv = f[::-1]
'''inv = ''
for l in range(len(f)-1, -1, -1):
    inv += f[l]'''
print('O inverso de {} é {}'.format(f, inv))
if f == inv:
    print('É um palíndromo')
else:
    print('NÃO é um palíndromo')
