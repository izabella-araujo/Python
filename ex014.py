import math
a=int(input('Qual o valor do cateto oposto?'))
b=int(input('Qual o valor do cateto adjacente?'))
h=(a**2 + b**2)**(1/2)
print('O comprimento da hipotenusa é: {}'.format(h))

from math import hypot
a=float(input('Qual o cateto oposto?'))
b=float(input('Qual o cateto adjacente?'))
h=hypot(a,b)
print('A hipotenusa é: {:.2f}'.format(h))

        