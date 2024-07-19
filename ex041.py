print('\033[33m-'*35)
print('\033[34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[33m-\033[m'*35)
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = 2024 - ano
if idade <= 9:
    print('CATEGORIA: \033[34mMIRIM')
elif idade > 9 and idade <=14:
    print('CATEGORIA: \033[31mINFANTIL')
elif idade >14 and idade <=19:
    print('CATEGORIA: \033[32mJUNIOR')
elif idade == 20:
    print('CATEGORIA: \033[35mSÊNIOR')
else:
    print('CATEGORIA: \033[36mMASTER')