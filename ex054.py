menores = 0
maiores = 0
for c in range(1,8):
    ano = int(input('Em que ano você nasceu? '))
    if 21 > 2024 - ano:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('A quantidade de pessoas menores de idade é {}'.format(menores))
print('A quantidade de maiores de idade é {}'.format(maiores))