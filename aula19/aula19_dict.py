pessoas = {'nome': 'Rafael', 'sexo': 'm', 'idade': 28}
print(pessoas)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print()
# del pessoas['sexo']
pessoas['nome'] = 'Pedro'
pessoas['peso'] = 90
for k, v in pessoas.items():
    print(f'{k}: {v}')
