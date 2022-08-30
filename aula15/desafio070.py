gtot = milmais = vmaisb = c = 0
nmaisb = ''
while True:
    n = str(input('\nNome do produto: '))
    p = float(input('Preço do produto: R$'))
    gtot += p
    c += 1
    if p > 1000:
        milmais += 1
    if c == 1 or p < vmaisb:
        vmaisb = p
        nmaisb = n
    o = ' '
    while o not in 'sn':
        o = str(input('Continuar [S/N]? ')).lower().strip()[0]
    if o == 'n':
        break
print(f'\nGasto total da compra: R${gtot:.2f}')
print(f'Total de produtos acima de mil reais: {milmais}')
print(f'Nome do produto mais barato: {nmaisb} no valor de {vmaisb:.2f}')
