n = int(input('Digite um número: '))
print('\033[34m-'*12,
      '\nTABUADA DO {}'.format(n))
print(('-'*12),
      '\n{} x {:2} = {}'.format(n, 1, n),
      '\n{} x {:2} = {}'.format(n, 2, n*2),
      '\n{} x {:2} = {}'.format(n, 3, n*3),
      '\n{} x {:2} = {}'.format(n, 4, n*4),
      '\n{} x {:2} = {}'.format(n, 5, n*5),
      '\n{} x {:2} = {}'.format(n, 6, n*6),
      '\n{} x {:2} = {}'.format(n, 7, n*7),
      '\n{} x {:2} = {}'.format(n, 8, n*8),
      '\n{} x {:2} = {}'.format(n, 9, n*9),
      '\n{} x {} = {}'.format(n, 10, n*10))
print('-'*12)
