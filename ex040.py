a=float(input('qual o preço do produto?'))
print('{:.^40}'.format('FORMAS DE PAGAMENTO'))
print('[1] À vista no dinheiro ou cheque'
      '[2] Á vista no cartão'
      '[3] Em 2x no cartão'
      '[4] Em 3x no cartão')
p=int(input('Qual a forma de pagamento você deseja?'))
v=a*0.9
if p==1:
    print(f'se for à vista no dinheiro ou cheque o valor do produto será {v}')
elif p==2:
    d=a*0.95
    print(f'se for á vista no cartão o produto fica no valor de {d}')
elif p==3:
    print('O produto permanece com o preço normal')
elif p==4:
    o=a*1.20
    print(f'O produto custará {0}')

    