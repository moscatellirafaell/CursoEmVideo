n = input('Seu nome completo: ').strip()
print('Com letras maiúsculas: {}'.format(n.upper()),
      '\nCom letras minúsculas: {}'.format(n.lower()),
      '\nQuantidade de letras: {}'.format(len(n)-n.count(' ')),
      '\nQuantidade de letras no primeiro nome: {}'.format(n.find(' ')))
