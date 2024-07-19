total = 0
mil = 0
maisbarato = 0
cont = 0
barato = ''
while True:
    print('LOJA BARATA')
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    total += preço
    cont = cont + 1
    if preço > 1000:
        mil = mil+1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        barato = produto
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O total gasto na compra foi de {total}')
print(f'{mil} produtos custam mais de 1000 reais.')
print(f'O produto mais barato foi {barato} que custa R${maisbarato}')
