a = float(input('Primeiro lado do triângulo: '))
b = float(input('Segundo lado do triângulo: '))
c = float(input('Terceiro lado do triângulo: '))
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print('É possível formar um tiângulo EQUILÁTERO')
    elif a == b or b == c or a == c:
        print('É possível formar um tiângulo ISÓSCELES')
    elif a != b != c != a:
        print('É possível formar um tiângulo ESCALENO')
else:
        print('NÃO É POSSÍVEL formar um triângulo')
