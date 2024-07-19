casa = float(input('Valor da casa: R$ '))
salario = float(input('Sal[ario do comprador: R$ '))
finan = int(input('Quantos anos de financiamento? '))
prestação = casa / (finan * 12)
mínimo = salario * 30 /100
print('Para pagar a casa de {:.2f} em {} anos'.format(casa, finan), end='')
print(' a prestação será de R${:.2f}.'.format(prestação))
if prestação <=mínimo:
    print('Empréstimo pode ser \033[32mCONCEDIDO\033[m.')
else:
    print('Empréstimo \033[31mNEGADO\033[m.')