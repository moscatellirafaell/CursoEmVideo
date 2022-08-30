n = int(input('Quantidade de termos da sequência Fibonacci: '))
p = 0
s = 1
c = 2
print(p, p + s,  end=' ')
while c < n:
    f = p + s
    print(f, end=' ')
    c += 1
    p = s
    s = f
