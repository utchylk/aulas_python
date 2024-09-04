dic = {}
lista = list()
soma = 0
media = 0
while True:
    dic.clear()
    dic['nome'] = str(input('Nome: '))
    while True:
        dic['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dic['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    dic['idade'] = int(input('Idade: '))
    soma = soma + dic['idade']
    lista.append(dic.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'A média de idade é {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}')
print()
for p in lista:
    if p['idade'] >= media:
        print(f'Pessoas com idade acima da média: {p['nome']}.')
print('ENCERRADO!!!')