from random import randint
print('Estou pensando num número entre 1 e 10... Consegue adivinhar qual é?')
num = int(input('Que número o computador está pensando? '))
computador = randint(1,10)
while num != computador:
    if num < computador:
        print('Mais... Tente novamente,')
        num = int(input('Que número o computador está pensando? '))
    if num > computador:
        print('Menos... Tente novamente: ')
        num = int(input('Que número o computador está pensando? '))
print('Você acertou! O computador estava pensado {}.'.format(computador))