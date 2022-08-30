from datetime import date
ma = 0
me = 0
for c in range(1, 8):
    a = int(input('Ano em que a {}ª pessoa nasceu: '.format(c)))
    if date.today().year - a >= 18:
        ma += 1
    else:
        me += 1
print('\nAo todo temos {} pessoa(s) maior de idade e {} pessoa(s) menor de idade'.format(ma, me))
