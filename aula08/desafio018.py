from math import radians, sin, cos, tan
a = float(input('Valor do ângulo: '))
print('Seno: \033[34m{:.2f}\033[m'.format(sin(radians(a))), '\nCosseno: \033[35m{:.2f}\033[m'.format(cos(radians(a))),
      '\nTangente: \033[36m{:.2f}\033[m'.format(tan(radians(a))))
