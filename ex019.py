import random
nome = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome,nome2,nome3,nome4]
escolha = random.choice(lista)
print('O aluno sorteado para apagar o quadro foi {}'.format(escolha))