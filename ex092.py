from datetime import datetime
dic = dict()
dic['nome'] = (str(input('Nome: ')))
nasc = (int(input('Ano de nascimento: ')))
dic['idade'] = datetime.now().year - nasc
dic['ctps'] = (int(input('Carteira de trabalho (0 não tem): ')))
if dic['ctps'] != 0:
    dic['contratação'] = (int(input('Ano de contratação: ')))
    dic['Salário'] = ((int(input('Salário: R$'))))
    dic['aposentadoria'] = dic['idade'] + ((dic['ctps'] + 35) - datetime.now().year)
for k, v in dic.items():
    print(f'{k} tem valor {v}')
