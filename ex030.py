a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
c=int(input('Digite o terceiro número:'))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=b
if a>b and a>c:
    maior=a
if c>b and c>a:
    maior=c
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
print('--FIM--')
