s = 'a'
while s not in 'fm':
    s = str(input('Digite o sexo [m/f]: ')).strip().lower()[0]
    if 'f' != s != 'm':
        print('OPÇÃO INVÁLIDA\n')
