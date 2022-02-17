v=float(input('Qual a distâcia da viagem em Km?'))
if v<=200:
    paga=v*0.5
    print('Você pagará R$:{}'.format(paga))
else:
    valor =100 + (v - 200) * 0.45
    print('Você pagará R$:{}'.format(valor))
print('--FIM--')




