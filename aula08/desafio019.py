import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
l = [n1, n2, n3, n4]
print('\033[30;41m Aluno sorteado: {} \033[m'.format(random.choice(l)))
