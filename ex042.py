print('\033[31m-\033[m'*25)
print('\033[7;36mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[31m-\033[m'*25)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('\033[32mEsses segmentos podem formar um triângulo.\033[m')
    if s1 == s2 and s2 == s3 and s3 == s1:
        print('Esses segmentos formam um triângulo \033[33mEQUILÁTERO\033[m.')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('Esses segmentos formam um triângulo \033[33mISÓSCELES\033[m.')
    else:
        print('Esses segmentos formam um triângulo \033[31mESCALENO\033[m.')
else:
    print('\033[31mEsses segmento não podem formar um triângulo.\033[m')