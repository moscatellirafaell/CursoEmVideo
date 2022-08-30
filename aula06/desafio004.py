algo = input('Digite algo: ')
print('O tipo primitivo desse valor é \033[30;41m', type(algo),
      '\033[m\nÉ um número?', algo.isnumeric(),
      '\nÉ alfabético?', algo.isalpha(),
      '\nÉ alfanumérico?', algo.isalnum(),
      '\nEstá em minúsculas?', algo.islower(),
      '\nEstá em maiúsculas?', algo.isupper(),
      '\nEstá capitalizada?', algo.istitle(),
      '\nSó tem espaço?', algo.isspace())
