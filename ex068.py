from random import randint
v = 0
print('\033[31m-'*30)
print('\033[34mVamos jogar par ou ímpar')
print('\033[31m-\033[m'*30)
while True:
    n = int(input('Diga um valor: '))
    tipo = ' '
    while tipo not in 'IP':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        break
    cn = randint(1,11)
    s = n + cn
    print('-'*20)
    print(f'Você jogou {n} e o computador {cn}. Total deu {s}.', end ='')
    print('DEU PAR' if s % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if s % 2 == 0:
            print('Você venceu!')
            v = v + 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('Você venceu!!')
            v+=1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamente')
print(f'Game OVER. Você venceu {v} vezes')



