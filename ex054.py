from random import randint
num=randint(1,10)
a=int(input('Tente advinhar o número escolhido pelo computador entre 1 e 10:'))
while a!=num:
    a=int(input('O número não está correto. Tente novamente:'))
print('\033[32mO número escolhido está correto.')




