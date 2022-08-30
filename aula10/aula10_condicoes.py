n = input('Digite seu nome: ').strip()
if n.lower() == 'rafael':
    print('\033[31mBelo nome!\033[m')
else:
    print('\033[34mApenas um nome comum...\033[m')
print('Bom dia, {}.'.format(n))
