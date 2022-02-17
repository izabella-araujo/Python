a=int(input('Qual o primeiro número?'))
b=int(input('Qual o segundo número?'))
if a>b:
    print('O número {} é o maior {} o menor'.format(a, b))
elif a<b:
    print('O número {} é o maior e o {} é o menor'.format(b, a))
elif a==b:
    print('Os dois valores são iguais')
