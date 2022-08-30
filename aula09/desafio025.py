n = input('Seu nome completo: ')
print('Tem \033[4mSilva\033[m no nome? \033[30;41m', 'silva' in n.lower(), end=' \033[m')
