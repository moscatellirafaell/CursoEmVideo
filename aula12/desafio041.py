from datetime import date
a = int(input('Ano de nascimento do atleta: '))
if date.today().year - a <= 9:
    print('CATEGORIA MIRIM')
elif date.today().year - a <= 14:
    print('CATEGORIA INFANTIL')
elif date.today().year - a <= 19:
    print('CATEGORIA JUNIOR')
elif date.today().year - a <= 25:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
