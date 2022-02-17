v=int(input('Qual a velocidade do carro?'))
if v>80:
    multa=(v-80)*7
    print('Você foi multado e deverá pagar o valor de R$:{},00'.format(multa))
else:
    print('Tudo certo!')
print('--FIM--')
