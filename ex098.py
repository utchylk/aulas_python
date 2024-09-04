from time import sleep
def contagem(ini, fi, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print('-'*30)
    print(f'Contagem de {ini} até {fi} de {pas} em {pas}')
    sleep(0.5)

    if ini < fi:
        cont = ini
        while cont <= fi:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += pas
        print('FIM!')
    else:
        cont = ini
        while cont >= fi:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont = cont - pas
        print('FIM!')
        print('-'*30)


contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)

