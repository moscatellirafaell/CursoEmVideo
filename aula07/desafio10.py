r = float(input('Quantos reais deseja trocar? R$'))
d = r / 3.27
print('\033[3mQuantidade em dólar:\033[m \033[3;33mUS${:.2f}\033[m'.format(d))
