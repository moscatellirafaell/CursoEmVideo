from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
l = [n1, n2, n3, n4]
shuffle(l)
print('\033[30;42m Ordem de apresentação: {} \033[m'.format(l))
