p = float(input('preço do produto: R$'))
f = int(input('Forma de pagamento:\n[1] à vista dinheiro/ pix\n[2] débito\n[3] crédito 2x\n[4] crédito 3x ou mais\n>>> '))
if f == 1:
    print('Valor: R${:.2f}'.format(p * 0.9))
elif f == 2:
    print('Valor: R${:.2f}'.format(p * 0.95))
elif f == 3:
    print('Valor da parcela: 2x de R${:.2f}'.format(p / 2), '\nValor total: R${:.2f}'.format(p))
elif f == 4:
    v = int(input('Quantas parcelas? '))
    print('Valor da parcela: {}x de R${:.2f}'.format(v, (p * 1.2) / v), '\nValor total: R${:.2f}'.format(p * 1.2))
