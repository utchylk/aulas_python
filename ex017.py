import math
catop = float(input('comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente'))
hip = math.sqrt(catop**2 + catadj**2)
print('O valor da hipotenusa é {}'.format(hip))