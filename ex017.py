from random import shuffle
a=str(input('primeiro aluno'))
b=str(input('Segundo aluno'))
c=str(input('Terceiro aluno'))
d=str(input('Quarto aluno'))
lista=(a, b, c, d)
ordem=shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

