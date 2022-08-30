n = int(input('Digite um número: '))
if n % 2 == 1:
    print('\033[1;40;3m Número ÍMPAR \033[m')
else:
    print('\033[1;40;3m Número PAR \033[m')
