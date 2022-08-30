d = int(input('Dias de aluguel do carro: '))
km = float(input('Kms rodados: '))
v = (d * 60) + (km * 0.15)
print('\033[30;42m Valor a ser pago pelo aluguel do carro: \033[30;41m R${:.2f} \033[m'.format(v))
