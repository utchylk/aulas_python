print('-='*20)
print('\033[34mANALISADOR DE TRIÂNGULOS\033[m')
print('-='*20)
t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('\033[32mEsses segmentos podem formar um triângulo.')
else:
    print('\033[31mEsses segmentos não podem formar um triângulo.')