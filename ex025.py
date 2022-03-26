import random
num=random.randint(1, 5)
a=int(input('Qual o número aparecerá entre 1 e 5:'))
if num==a:
    print('O número é {} e você escolheu {}, então você venceu'.format(num, a))
else:
    print('O número foi {} e você escolheu {}, então você perdeu'. format(num, a))
print('--FIM--')






