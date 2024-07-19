km = float(input('Quantos quilômetros foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco = (km*0.15) + (dias*60)
print('O preço a pagar pelo carro alugado é de R${:.2f}.'.format(preco))