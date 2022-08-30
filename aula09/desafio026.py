f = input('Digite uma frase: ').strip().lower()
print('Quantas letras A: {}'.format(f.count('a')),
      '\nQual posição aparece pela primeira vez: {}'.format(f.find('a')+1),
      '\nQual posição aparece pela última vez: {}'.format(f.rfind('a')+1))
