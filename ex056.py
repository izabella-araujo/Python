from math import factorial
a=int(input('Digite um número:'))
if a<0:
    print('Não existe fatorial de número negativo')
elif a==0:
    print('O fatorial do número zero é 1')
else:
    f=1
    while a>1:
        f*=a
        a-=1
    print('O fatorial do número escolhido é {}'.format(f))



