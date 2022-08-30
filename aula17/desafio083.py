ex = str(input('Digite a expressão: '))
pa = []
pf = []
for c in ex:
    if c == '(':
        pa.append(c)
    elif c == ')':
        pf.append(c)
if len(pa) == len(pf):
    print('Expressão válida')
else:
    print('Expressão inválida')
