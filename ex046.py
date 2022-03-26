soma=0
cont=0
for c in range(1,7):
    a=int(input('Digite o {}:'.format(c)))
    if a%2==0:
        soma+=a
        cont+=1
print('Tem {} números pares e a soma desses números é {}'.format(cont, soma))
