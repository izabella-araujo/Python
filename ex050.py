tot=0
cont=0
for c in range(1,8):
    a=int(input('Qual sua idade?'))
    if a>=18:
        tot+=1
    else:
        cont+=1
print('{} pessoas são de menor e {} pessoas são de maiores'.format(cont, tot))



