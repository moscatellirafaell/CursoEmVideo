a = float(input('Sua altura (m): '))
p = float(input('Seu peso (kg): '))
imc = p / (a * a)
if imc < 18.5:
    print('IMC: {:.1f}'.format(imc), '\nAbaixo do peso')
elif 25 > imc >= 18.5:
    print('IMC: {:.1f}'.format(imc), '\nPeso ideal')
elif 30 > imc >= 25:
    print('IMC: {:.1f}'.format(imc), '\nSobrepeso')
elif 40 > imc >= 30:
    print('IMC: {:.1f}'.format(imc), '\nObesidade')
else:
    print('IMC: {:.1f}'.format(imc), '\nObesidade mórbida')
