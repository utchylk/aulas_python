matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
soma3 = 0
mai2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} e {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
        if matriz[1][c] > mai2:
            mai2 = matriz[1][c]
        if matriz[l][c] == matriz[l][2]:
            soma3 = soma3 + matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print(f'A soma de todos os valores pares digitados é {somapar}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {mai2}')