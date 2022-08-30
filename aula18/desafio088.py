from random import randint
lista = []
jogos = []
q = int(input('quantidade de jogos: '))
while q > 0:
    while len(lista) < 6:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
    jogos.append(lista[:])
    lista.clear()
    q -= 1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {sorted(l)}')
