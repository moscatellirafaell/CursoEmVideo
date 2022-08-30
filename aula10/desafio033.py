a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))
me = a
if b < a and b < c:
    me = b
if c < a and c < b:
    me = c
ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c
print('Maior número: {}'.format(ma))
print('Menor número: {}'.format(me))
