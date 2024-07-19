n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    c = c + 1
    s = s + n
print('Você digitou {} números e a soma entre eles é {}'.format(c-1, s-999))
print('ACABOU')
