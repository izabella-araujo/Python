soma=cont=num=0
num=int(input('Digite um número:'))
while num!=999:
    num=int(input('Digite um número:'))#repete aqui para não contar com o fleg na hora da soma e do cont#
    cont+=1
    soma+=num
print('você digitou {} números e a soma entres eles é {}'.format(cont, soma))
