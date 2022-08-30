s = int(input('Valor do saque: R$'))
cedval = 50
cedtot = 0
while True:
    if s >= cedval:
        s -= cedval
        cedtot += 1
    else:
        print(f'{cedtot} cédulas de R${cedval:.2f}')
        if cedval == 50:
            cedval = 20
        elif cedval == 20:
            cedval = 10
        elif cedval == 10:
            cedval = 1
        cedtot = 0
        if s == 0:
            break
