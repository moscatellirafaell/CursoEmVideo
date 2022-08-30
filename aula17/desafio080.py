val = list()
valord = list()
mai = men = 0
for c in range(0, 5):
    val.append(int(input('Digite um valor: ')))
    if c == 0:
        mai = val[-1:]
        valord.append(val[-1:])
    if val[-1:] > mai:
        mai = val[-1:]
        valord.append(val[-1:])
print(mai)
print(valord)
