l = float(input('Largura da parede(m): '))
a = float(input('Altura da parede(m): '))
aa = l * a
t = aa / 2
print('Serão  necessários \033[1;31m{:.1f} litros\033[m de tinta para pintar essa parede'.format(t))
