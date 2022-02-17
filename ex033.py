v=int(input('Qual o valor da casa?'))
a=int(input('Qual o valor do seus salário?'))
p=int(input('Em quantos anos deseja pagar a casa?'))
s=v/(p*12)
if s<=0.30*a:
    print('A prestação será de {}'.format(s))
else:
    print('O empréstimo foi negado')
