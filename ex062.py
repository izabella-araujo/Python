from random import randint
v=0
while True: #enquanto infinito#
    jogador=int(input('Digite um valor:'))
    computador=randint(0,10)
    total=jogador + computador
    tipo=' '
    while tipo not in 'PIÍ': #enquanto não digitar certo vai repetir a pergunta#
        tipo=str(input('Par ou ímpar? ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o camputador {computador}. totalizando {total}',  end=' ')
    print('DEU PAR' if total%2==0 else 'DEU ÍMPAR')
    if tipo=='P':
        if total%2==0:
            print('VOCÊ GANHOU!!!')
            v+=1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo=='IÍ':
        if total%2==1:
            print('VOCÊ GANHOU!!!')
            v+=1
        else:
            print('VOCÊ PERDEU!')
            break #para sair de um loop#
    print(f'Você ganhou {v} vezes')





