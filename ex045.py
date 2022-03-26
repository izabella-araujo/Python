#só o resultado#
c=int(input('Escolhe um número:'))
for a in range(1,11):
    a=a*c
    print(a)
#ou assim#
c=int(input('Escolhe um número:'))
for a in range(1,11):
    print('{} x {:2} = {}'.format(c, a, c*a))



