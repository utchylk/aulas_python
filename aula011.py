a = 'Lucas'
b = 'Breno'
cores = {'limpa': '\033[m',
         'azul': '\033[034m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
print('{}{}{} e {}{}{} são lindos.'.format(cores['verde'], b, cores['limpa'], cores['azul'], a, cores['limpa']))
#print('\033[32m{}\033[m e \033[34m{}\033[m são lindos'.format(b, a))
#print('{}{}{} e {}{}{} são lindos.'.format('\033[32m', b ,'\033[m', '\033[34m', a, '\033[m'))
res = str(input('Você concorda? '))
res = res.lower().strip()
if res == 'sim' or res == 's':
    print('Ebaaaaaa! Que bom! :)')
else:
    print('Se liga! >:C')