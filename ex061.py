resp='Ss'
soma=quant=media=menor=maior=0
while resp in 'Ss':
    num=int(input('Digite um núemro:'))
    soma+=num
    quant+=1
    if quant==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resp=str(input('Você quer continuar?')).upper().strip()[0]
media=soma/quant
print('Você digitou {} números e a média desses números é {}').fotmat(quant,media)
print=('O maior número é {} e o menor {}').format(maior, menor)
