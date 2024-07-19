print('\033[1;31mTABUADA\033[m')
n = int(input('Você quer ver a tabuada de que número?: '))
for c in range(1, 11):
    r = n*c
    print('{}x{}={}'.format(c, n, r))