v = int(input('Velocidade atingida pelo veículo (km/h): '))
if v > 80:
    print('\033[1;31mLimite de velocidade ultrapassado!\033[m\nValor da multa: R${}'.format((v - 80) * 7))
else:
    print('\033[35mVelocidade dentro do limite permitido')
