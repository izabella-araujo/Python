total=totmil=menor=cont=0
barato=''
while True:
    produto=str(input('Qual o nome do produto?'))
    preço=float(input('Qual o preço? R$:'))
    cont+=1
    total+=preço
    if preço>1000:
        totmil+=1
    if cont==1 or preço<menor: #o primeiro preço é o maior e o menor pq só tem ele#
        menor=preço
        barato=produto
    resp=''
    while resp not in 'SN':
        resp=str(input('Você quer continuar?[S/N]')).upper().strip()[0]
    if resp=='N':
        break
print(f'O total da compra foi R$:{total:.2f}')
print(f'Tem {totmil} produto acima de R$:1000,00 '
      f'e o mais barato é {barato} com o valor de R$:{menor:.2f}')
