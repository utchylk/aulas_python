nome = str(input('Digite o seu nome: ')).strip()
print('Quantidade de vezes que a letra "A" aparece no seu nome: {}'.format(nome.upper().count('A')))
print('A letra "A" aparece pela primeira vez no seu nome na posição {}.'.format(nome.upper().find('A')+1))
print('A letra "A aparece pela última vez no seu nome na posição {}.'.format(nome.upper().rfind('A')+1))