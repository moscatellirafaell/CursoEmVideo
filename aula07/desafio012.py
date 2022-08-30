p = float(input('Preço do produto: R$'))
d = p * 0.95
print('Preço do produto com 5% de desconto:\033[1;30;42m R${:.2f} \033[m'.format(d))
