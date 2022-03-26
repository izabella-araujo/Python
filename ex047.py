cont=0
a=float(input('Qual o primeiro termo?'))
b=float(input('Qual a razão?'))
for c in range(1,11):
    cont+=1
    t=a+(cont-1)*b
    print('O termo {} é {}'.format(cont,t))
