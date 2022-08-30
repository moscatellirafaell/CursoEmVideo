n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('\033[40m Dobro: {} \033[m\n\033[40m Triplo: {} \033[m\n\033[40m Raíz Quadrada: {:.2f} \033[m'.format(d, t, r))
