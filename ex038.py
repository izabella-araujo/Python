a=float(input('Qual a medida do cateto oposto?'))
b=float(input('Qual  a medida do cateto adjacente?'))
c=float(input('Qual a medida da hipotenusa?'))
if a<b+c and b<a+c or c<a+b:
    print('As medidas {}, {}, {}, formam um triângulo'.format(a, b, c))
print('Classificação de triângulo')
if a==b==c:
    print('O triângulo é equilátero')
elif a==b!=c or c==b!=a:
    print('O triângulo é isósceles')
elif a!=b!=c:
    print('O triângulo é escaleno')
    
