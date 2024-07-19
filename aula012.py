nome = str(input('Qual o seu nome? ')).strip()
nome = nome.upper()
if nome == 'LUCAS':
    print('Que nome lindo!')
elif nome == 'BRENO':
    print('Seu nome é MUITO LINDO!!!')
else:
    print('Que nome normal.')
print('Prazer em te conhecer, {}!'.format(nome))
