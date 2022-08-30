c = input('Nome de uma cidade: ')
print('Começa com a palavra \033[4mSanto\033[m? \033[30;41m', 'santo' in c.lower(), end=' \033[m')
