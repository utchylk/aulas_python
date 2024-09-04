lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
    for i, v in enumerate(lista):
        if v % 2 == 0:
            par.append(v)
        elif v % 2 == 1:
            impar.append(v)
print(f'Os valores pares digitados foram {par}')
print(f'Os valores ímpares digitados foram {impar}')