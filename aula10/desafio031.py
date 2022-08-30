d = int(input('Distância da viagem (km): '))
if d <= 200:
    print('Preço da passagem: R${:.2f}'.format(d * 0.5))
else:
    print('Preço da passagem: R${:.2f}'.format(d * 0.45))
