lanche = 'hamburger', 'suco', 'pizza', 'pudim'

print('')

for c, comida in enumerate(lanche):
    print(c, comida)

print('')

for cont in range(0, len(lanche)):
    print(cont, lanche[cont])
    
print('')
print(sorted(lanche))
