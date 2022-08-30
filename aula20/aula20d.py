def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


val = [3, 5, 7, 1]
dobra(val)
print(val)
