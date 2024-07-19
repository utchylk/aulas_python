from random import randint
print('Estou pensando num número entre 0 e 5... Consegue adivinhar qual é?')
num = int(input('Que número o computador está pensando? '))
computador = randint(0,5)
if num == computador:
    print('PARABÉNS! Você acertou!')
else:
    print('Sinto muito, você errou! :(')
print('O número que pensei foi {}.'.format(computador))

