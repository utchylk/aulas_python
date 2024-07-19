r = 'S'
pares = 0
impares = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    if n != 0:
        if n % 2 ==0:
            pares += 1
        else:
            impares += 1
print('Você digitou {} números pares e {} números ímpares.'.format(pares, impares))