n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, total))
if total == 2:
    print('E por isso ele \033[32mé \033[m primo.')
else:
    print('E por isso ele \033[31mnão\033[m é primo.')