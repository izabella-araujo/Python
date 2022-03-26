cont=tot=ger=0
while True:
    a = int(input('Qual a sua iade?'))
    b =''
    while b not in 'FM':
        b = str(input('Qual o seu sexo?[F/M]')).upper().strip()[0]
    if a>18:
        cont+=1
    if b=='M':
        tot+=1
    if b=='F' and a<20:
        ger+=1
    resp=''
    while resp not in 'SN':
        resp = str(input('Você deseja continuar?')).upper().strip()[0]
    if resp=='N':
        break
print(f'No total de pessoas cadastradas {cont} é maior de 18 anos'
          f', {tot} é homem '
          f'e {ger} é mulher e tem menos de 20 anos')







