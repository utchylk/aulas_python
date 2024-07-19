n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n3)/3
print('Sua média é {}'.format(m))
if m <5.0:
    print('\033[1;31mREPROVADO')
elif m>=5.0 and m<6.9:
    print('\033[1;33mRECUPERAÇÃO')
else:
    print('\033[32mAPROVADO')