num = list()
pares = list()
impares = list()
for c in range(1,8):
    num.append(int(input(f'Digite o {c}o valor: ')))
    for n in num:
        if n % 2 == 0:
            pares.append(num[:])
        else:
            impares.append(num[:])
    num.clear()
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram {impares}')