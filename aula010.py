#nome = str(input('Qual o seu nome? '))
#if nome.lower() == 'Lucas':
    #print('Que nome lindo você tem!')
#else:
    #print('Que nome normal...')
#print('Prazer em te conhecer, {}!'.format(nome))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Sua média foi {}.'.format(media))
if media >=6:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')