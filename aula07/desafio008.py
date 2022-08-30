m = float(input('Digite o valor em metros: '))
cm = m * 100
mm = m * 1000
print('Centímetros: \033[3m{:.0f}cm\033[m\nMilímetros: \033[3m{:.0f}mm\033[m'.format(cm, mm))
