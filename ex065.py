n = 0
resp = 'S'
média = 0
soma = 0
quant = 0
maior = 0
menor = 0
while resp in 'Sn':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

média = soma/quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
#print('A média entre os números digitados é {}'.format())
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
