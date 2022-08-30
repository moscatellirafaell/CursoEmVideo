n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[3mMédia: {:.1f}'.format(m), '\033[m\n\033[1;31mREPROVADO\033[m')
#elif m >= 5 and m < 7:
elif 7 > m >= 5:
    print('\033[3mMédia: {:.1f}'.format(m), '\033[m\n\033[1;34mRECUPERAÇÃO\033[m')
else:
    print('\033[3mMédia: {:.1f}'.format(m), '\033[m\n\033[1;32mAPROVADO\033[m')
