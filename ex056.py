somaidade = 0
médiaidade = 0
maisvelhoidade = 0
maisvelhonome = ''
mulheres = 0
for c in range(1,5):
    print('-------{}ª PESSOA-------'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    média = idade * c / 4
    if c == 1 and sexo in 'Mm':
        maisvelhoidade = idade
        maisvelhonome = nome
    if sexo in 'Mm' and idade >maisvelhoidade:
        maisvelhoidade = idade
        maisvelhonome = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelhoidade, maisvelhonome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))