v1 = int(input('Diga o primeiro valor: '))
v2 = int(input('Diga o segundo valor: '))
if v1 > v2:
    print('O \033[32mprimeiro\033[m valor é maior.')
elif v2 > v1:
    print('O \033[33msegundo\033[m valor é maior.')
else:
    print('\033[31mNão existe\033[m valor maior, os dois são iguais.')