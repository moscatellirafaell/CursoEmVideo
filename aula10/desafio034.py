s = float(input('Salário atual: R$'))
if s > 1250:
    print('Novo salário: R${:.2f}'.format(s * 1.1))
else:
    print('Novo salário: R${:.2f}'.format(s * 1.15))
