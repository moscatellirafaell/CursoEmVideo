n = int(input('Digite um número: '))
c = int(input('Escolha a base de conversão:\n[1] binário\n[2] octal\n[3] hexadecimal\n>>> '))
if c == 1:
    print(bin(n)[2:])
elif c == 2:
    print(oct(n)[2:])
elif c == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida. Tente novamente')
