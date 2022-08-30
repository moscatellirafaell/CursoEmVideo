alunos = []
notasg = []
notasi = []
medias = []
while True:
    al = str(input('Aluno: '))
    alunos.append(al)
    n1 = float(input('Nota 1: '))
    notasi.append(n1)
    n2 = float(input('Nota 2: '))
    notasi.append(n2)
    notasg.append(notasi[:])
    notasi.clear()
    m = (n1 + n2) / 2
    medias.append(m)
    op = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    print()
    if op == 'n':
        break
print('=-'*13)
print('{:<5}{:<13}{:>4}'.format('Nº', 'ALUNO', 'MÉDIA'))
print('-'*25)
for n, a in enumerate(alunos):
    print(f'{n:<5}{a:<13}{medias[n]:>4}')
print('=-'*13)
print()
while True:
    op2 = int(input('Mostrar notas de qual aluno (999 P/ ENCERRAR)? '))
    if op2 == 999:
        break
    for n, a in enumerate(alunos):
        if op2 == n:
            print(f'Notas de {a}: {notasg[n]}')
    print()
