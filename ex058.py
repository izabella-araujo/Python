a=int(input('Qual o primeiro termo ds PA?'))
b=int(input('Qual a razão da PA?'))
termo=a
cont=total=0
while cont>=10:
    print=('{}'.format(termo, end=''))
    termo+=b
    cont+=1
mais=10
while mais !=0:
    total+=mais
    while cont <=total:
        print('{}'.format(termo, end=''))
        termo+=b
        cont+=1
    print('PAUSE')
    mais=int(input('Quantos termos você quer mostrar a mais?'))
    