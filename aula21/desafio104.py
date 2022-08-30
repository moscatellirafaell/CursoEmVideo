def leiaInt():
    while True:
        n = input('Digite um número: ').strip()
        if n.isnumeric():
            return n
        else:
            print('\033[31mERRO! Digite um número válido\033[m')
            print()


print(f'Você digitou o número {leiaInt()}')
