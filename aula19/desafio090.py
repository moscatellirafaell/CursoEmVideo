aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 7 > aluno['media'] >= 5:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print()
for k, v in aluno.items():
    print(f'{k}: {v}')
