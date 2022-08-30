n = input('Seu nome: ').strip()
if n.lower() == 'rafael':
    print('Belo nome!')
elif n.lower() == 'pedro' or n.lower() == 'maria' or n.lower() == 'paulo':
    print('Nome bem popular')
elif n.lower() in 'ana claudia jessica juliana':
    print('Belo nome feminino!')
#else: >>>>>> pode ficar oculto nesse caso
print('Nome comum...')
