print('='*20)
print('\033[31m{:^20}\033[m'.format('BANCO CEV'))
print('='*20)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cédula = 50
totalcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcéd = 0
        if total == 0:
            break
