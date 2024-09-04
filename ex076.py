listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Trasnferidor', 15.90,
            'Compasso', 9.99)
print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>10.2f}')