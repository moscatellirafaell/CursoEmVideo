def cont(*num):
    print(sorted(num))


def soma(*num):
    s = 0
    for n in num:
        s += n
    print(s)


cont(2, 1, 3)
cont(2)
cont(3, 7, 3, 6)
cont(3, 3, 5, 9, 5, 0)
print()
soma(2, 3)
soma(2, 3, 5)
