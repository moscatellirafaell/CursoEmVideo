pal = 'bolo', 'furadeira', 'papel', 'chocolate', 'cravo', 'suco', 'ovo', 'cocada'
for p in pal:
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')
    for l in p:
        if l in 'aeiou':
            print(l.upper(), end='  ')
