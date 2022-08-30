from time import sleep


def maior(* num):
    print('-' * 30)
    mai = 0
    for e, n in enumerate(num):
        if e == 0:
            mai = n
        if n > mai:
            mai = n
        print(n, end=' ')
        sleep(0.3)
    print(f'\nTotal de números: {len(num)}')
    print(f'Maior número: {mai}')
    print('-' * 30)
    sleep(1)
    print()


maior(1, 0, 7, 4, 8)
maior(9, 5, 3)
maior(2, 6)
maior(9)
maior()
