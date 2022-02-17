from random import choice
a=str(input('Primeiro aluno'))
b=str(input('Segundo aluno'))
c=str(input('Terceiro aluno'))
d=str(input('Quarto aluno'))
lista=(a, b, c, d)
escolhido=choice(lista)
print('O escolhido foi {}'.format(escolhido))
