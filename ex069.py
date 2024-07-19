tot18 = 0
homem = 0
totmulher20 = 0
r = ' '
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    sexo = ''
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if idade >= 18:
        tot18 += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O total de pessoas cadastradas com mais de 18 anos foi {tot18}')
print(f'{homem} homens foram cadastrados.')
print(f'{totmulher20} mulheres cadastradas tem menos de 20 anos')
