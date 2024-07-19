import random
t1 = input('Primeiro aluno: ')
t2 = input('Segundo aluno: ')
t3 = input('Terceiro aluno: ')
t4 = input('Quarto aluno: ')
ordem = [t1,t2,t3,t4]
random.shuffle(ordem)
print ('A ordem de trabalhos é: {}'.format(ordem))