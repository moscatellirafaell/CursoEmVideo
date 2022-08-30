s = float(input('Salário atual: R$'))
ns = s * 1.15
print('\033[3mNovo salário com 15% de aumento: \033[31mR${:.2f}'.format(ns))
