n = []
while True:
    n.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'Você digitou {len(n)} elementos.')
n.sort(reverse=True)
print(f'Os números que você digitou em ordem decrescente é: {n}')
if 5 in n:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')