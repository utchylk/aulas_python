primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        c += 1
    print('Pausa')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('FIMMMMMMMMMMMMM')