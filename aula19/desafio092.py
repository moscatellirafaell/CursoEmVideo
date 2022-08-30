from datetime import date
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano nascimento: '))
cadastro['Idade'] = date.today().year - nasc
if cadastro['Idade'] >= 18:
    cadastro['Contratação'] = int(input('Ano contratação: '))
    cadastro['Aposentadoria'] = (cadastro["Contratação"]+35) - nasc
    print()
    print(cadastro)
    for i in cadastro.items():
        print(f'{i[0]}: {i[1]}')
else:
    print('\nMenor de idade')
