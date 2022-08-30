from datetime import date
a = int(input('Seu ano de nascimento: '))
if date.today().year - a < 18:
    print('Falta(m) {} ano(s) para você se alistar ao serviço militar'.format((a - date.today().year) + 18))
elif date.today().year - a == 18:
    print('Você deve se alistar esse ano para o serviço militar')
elif date.today().year - a == 19:
    print('Já se passou 1 ano do prazo para você se alistar ao serviço militar')
elif date.today().year - a > 19:
    print('Já se passaram {} anos do prazo para você se alistar ao serviço militar'.format((date.today().year - a) - 18))
