r1=float(input('Digite o valor da primeira reta:'))
r2=float(input('Digite o valor da segunda reta:'))
r3=float(input('Digite o valor da terceira reta:'))
if r1>r2+r3 and r2>r1+r3 and r3>r1+r2:
    print('Os valores das retas podem formar um triângulo')
else:
    print('Os valores das retas não podem formar um triângulo')
print('--FIM--')
