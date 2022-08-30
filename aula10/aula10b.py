n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('\033[3mMédia: {:.1f}\033[m'.format(m))
if m >= 6:
    print('\033[30;42m APROVADO \033[m')
else:
    print('\033[30;41m REPROVADO \033[m')
