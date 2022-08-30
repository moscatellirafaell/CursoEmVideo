ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    ficha.append([nome, [n1, n2], media])
    op = str(input('Continuar? ')).strip().lower()[0]
    print()
    if op == 'n':
        break
print('=-'*13)
print(f'{"Nº":<5}{"ALUNO":<13}{"MÉDIA":>4}')
print('-'*25)
for n, a in enumerate(ficha):
    print(f'{n:<5}{a[0]:<13}{a[2]:>4}')
print('=-'*13)
print()
while True:
    op2 = int(input('Mostrar notas de qual aluno (999 P/ ENCERRAR)? '))
    if op2 == 999:
        break
    if op2 <= len(ficha)-1:
        print(f'Notas de {ficha[op2][0]}: {ficha[op2][1]}')
    print()
