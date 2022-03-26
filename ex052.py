#a media de idade do grupo, o nome do homem mais velho, quantas mulheres tem menos de 20 anos#
idade=0
media=0
maior=0
nome=''
tot=0
for c in range(1,5):
    print('------- {} PESSOA-------'.format(c))
    a=str(input('Qual o seu nome?'.strip( )))
    b=str(input('Qual o seu sexo [M/F]?'.strip( )))
    d=int(input('Qual a sua idade?'.strip( )))
    idade+=d
    media=idade/4
    if c==1 and b in 'Mm':
        maior=d
        nome=a
    if d>maior and b in 'Mm':
            maior=d
            nome=a
    if d<20 and b in 'Ff':
        tot+=1
print('A média da idade das pessoa é {}'.format(media))
print('O nome do homem mais velho é {}'.format(nome))
print('Nesse grupo tem {} mulheres com menos de 20 anos'.format(tot))







