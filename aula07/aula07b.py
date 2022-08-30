n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('\033[34mSoma: {}\nProduto: {}\nDivisão: {:.2f}\nDivisão inteira: {}\nPotência: {}'.format(s, m, d, di, e))
