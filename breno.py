from random import randint
from time import sleep
import os
itens = ('\033[37mPEDRA\033[m' , '\033[36mPAPEL\033[m' , '\033[35mTESOURA\033[m')
computador = randint(0,2)
print('-='*20)
print('PEDRA, PAPEL, TESOURA')
print('-='*20)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
if jogador >= 3:
    print('JOGADA INVÁLIDA. Tente novamente')
    exit()
os.system('cls')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print ('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('\033[37mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mJogador venceu\033[m')
    elif jogador == 2:
        print('\033[31mComputador venceu\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[31mComputador venceu\033[m')
    elif jogador == 1:
        print('\033[37mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mJogador venceu\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[32mJogador venceu\033[m')
    elif jogador == 1:
        print('\033[31mComputador venceu\033[m')
    elif jogador == 2:
        print('\033[37mEMPATE\033[m')