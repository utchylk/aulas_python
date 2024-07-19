nasc = int(input('Informe seu ano de nascimento: '))
alis = 2024-nasc
if alis < 18:
    print('\033[31mNão está na hora de você se alistar ainda.')
elif alis == 18:
    print('\033[36mEstá na hora de você se alistar.')
else:
    alis = alis - 18
    print('Já passou o tempo do seu alistamento há \033[34m{} anos.'.format(alis))