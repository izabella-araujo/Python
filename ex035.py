i=int(input('Qual a sua idade?'))
if i<18:
    f=18-i
    print('falta {} anos para seu alistamento'.format(f))
elif i==18:
    print('Está na hora de se alistar')
elif i>18:
    g=i-18
    print('Faz {} anos que passou do tempo do seu alistamento'.format(g))

