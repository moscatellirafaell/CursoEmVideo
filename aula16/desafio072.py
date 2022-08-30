ext = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
while True:
    num = int(input('Digite um número de 0 à 10: '))
    if 0 <= num <= 10:
        break
print(ext[num])
while True:
    o = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    if o == 'n':
        break
    if o == 's':
        num = int(input('Digite um número de 0 à 10: '))
        print(ext[num])
