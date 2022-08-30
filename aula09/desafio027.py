n = input('Digite seu nome completo: ').strip()
s = n.split()
print('Primeiro nome: {}'.format(s[0]),
      '\nÚltimo nome: {}'.format(s[len(s)-1]))
