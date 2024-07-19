dist = float(input('Qual a distância da viagem em km? '))
if dist <=200:
    preco = dist*0.50
    print('O valor dessa viagem será de R${}.'.format(preco))
else:
    preco = dist*0.45
    print('O valor dessa viagem será de R${}.'.format(preco))