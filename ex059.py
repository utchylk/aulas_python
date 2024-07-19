n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != '5':
    print('''   [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = str(input('>>>>>>>Qual é a sua opção? '))
    if opção == '1':
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1+n2))
    if opção == '2':
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1*n2))
    if opção == '3':
        if n1 > n2:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n1))
        else:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n2))
    if opção == '4':
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
print('Fim do programa. Volte sempre!')
