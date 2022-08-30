a = float(input('Primeiro lado do triângulo: '))
b = float(input('Segundo lado do triângulo: '))
c = float(input('Terceiro lado do triângulo: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
