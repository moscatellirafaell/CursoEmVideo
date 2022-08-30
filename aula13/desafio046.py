from time import sleep
print('\033[7;40m=\033[m'*35)
print('\033[1;7;40mCONTAGEM REGRESSIVA PARA O ANO NOVO\033[m')
print('\033[7;40m=\033[m'*35)
sleep(1)
for c in range(10, 0, -1):
    print('\033[3m', c, '...\033[m')
    sleep(1)
print('\033[33m*\033[m'*17)
print('\033[1;34mFELIZ ANO NOVO!!!\033[m')
print('\033[33m*\033[m'*17)
