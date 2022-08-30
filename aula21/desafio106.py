from time import sleep


def pyHelp():
    while True:
        msg = 'SISTEMA DE AJUDA PyHELP'
        print('-' * (len(msg)+4))
        print(f'  {msg}')
        print('-' * (len(msg)+4))
        op = str(input('Função ou Biblioteca: ')).lower()
        if op == 'fim':
            msg = 'ATÉ LOGO!'
            print('Encerrando...')
            sleep(1)
            print('-' * (len(msg) + 4))
            print(f'  {msg}')
            print('-' * (len(msg) + 4))
            break
        elif op == '':
            print('\n\033[31mErro!\nTente novamente\033[m')
            print()
        else:
            msg = f"Acessando o manual do comando '{op}'..."
            print(f'{msg}')
            sleep(1.5)
            print('\033[32m')
            help(op)
            print('\033[m')


pyHelp()
