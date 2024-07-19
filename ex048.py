s = 0
print('Números ímpares que são divisíveis por 3')
n = int(input('ajdibadji: '))
for c in range(1, n, 2):
    if c % 3 == 0:
        s = s + c
print('A soma entre todos os números ímpares divisíveis por 3 até {} é {}'.format(n, s))
