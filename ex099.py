from time import sleep


def cont(*num):
    mai = 0
    tam = len(num)
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='')
        sleep(1)
        if c > mai:
            mai = c
        if c == 0 and tam == 1:
            tam = 0
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor foi {mai}')


cont(3, 4)
cont(3, 8, 1, 2, 9)
cont(6, 9, 5, 6, 3)
cont(7, 1)
cont(0)
