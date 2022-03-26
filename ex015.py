from math import sin, cos,tan, radians
a=float(input('Qual o valor do ângulo?'))
seno=sin(radians(a))
print('O ângulo de {} tem o seno {:.2f}'.format(a, seno))
cosseno=cos(radians(a))
print('Quando o ângulo for {} o cosseno será: {:2f}'.format(a, cosseno))
tangente=tan(radians(a))
print('Quando o ângulo for {} a tangente será: {:2f}'.format(a, tangente))

