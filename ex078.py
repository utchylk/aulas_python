num = []
mai = 0
men = 0
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        mai = men = num[n]
    else:
        if num[n] > mai:
            mai = num[n]
        if num[n] < men:
            men = num[n]
print(f'O maior valor digitado foi {mai} na posição', end= ' ')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end = '')
print(f'\nO menor valor digitado foi {men} na posição', end = ' ')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end = '')