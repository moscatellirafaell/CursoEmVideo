s = int(input('Valor do saque: R$'))
while True:
    cin = s // 50
    if cin > 0 and s > 0:
        print(f'{cin} cédulas de R$50')
    s %= 50
    vin = s // 20
    if s > 0 and vin > 0:
        print(f'{vin} cédulas de R$20')
    s %= 20
    dez = s // 10
    if s > 0 and dez > 0:
        print(f'{dez} cédulas de R$10')
    s %= 10
    um = s
    if s > 0 and um > 0:
        print(f'{um} cédulas de R$1')
    break
