def voto(a):
    from datetime import date
    i = date.today().year - a
    print(f'Idade: {i}')
    if i < 16:
        return 'AINDA NÃO VOTA'
    elif 16 <= i < 18 or i > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


ano = int(input('Ano de nascimento: '))
print(voto(ano))
