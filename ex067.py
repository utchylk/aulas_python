while True:
    print('-'*20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    r = 0
    print('-'*20)
    for c in range(1, 10):
        if n < 0:
            print('Programa encerrado.')
            break
        r = n*c
        print(f'{n} x {c} = {r}')

