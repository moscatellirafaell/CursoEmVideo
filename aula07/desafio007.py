n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('Média: \033[30;41m {:.1f} \033[m'.format(m))
