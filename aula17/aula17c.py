a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'lista a: {a}')
print(f'lista b: {b}')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'\nlista a: {a}')
print(f'lista b: {b}')
