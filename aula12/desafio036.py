c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Pagar em quantos anos? '))
m = (c / a) / 12
if m <= s * 0.3:
    print('\033[3mValor da mensalidade: R${:.2f}'.format(m),
          '\nRepresentando {:.1f}% do seu salário'.format(m * 100 / s))
else:
    print('O valor da mensalidade excede 30% do salário\nCom valor de R${:.2f}, representando {:.1f}%'.format(m, m * 100 / s))
