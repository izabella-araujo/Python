a=float(input('Qual foi sua primeira nota?'))
b=float(input('Qual foi sua segunda nota?'))
m=(a+b)/2
if m<5:
    print('Você, infelizmente, foi reprovado')
elif 5<m<6.9:
    print('Você está em recuperação, estude mais.')
elif m>7:
    print('Você está aprovado, parabéns!')

