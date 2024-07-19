#n = int(input('Digite um valor para calcular a fatorial: '))
#c = n
#f = 1
#print('Calculando {}! = '.format(n), end='')
#while c > 0:
    #print('{}'.format(c), end='')
    #print(' x ' if c > 1 else ' = ', end='')
    #f = f * c
    #c -= -1
#print('{}'.format(f))
n = int(input('Digite um valor para calcular o fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c >1 else ' = ', end='')
    f *= c
print('{}'.format(f))
