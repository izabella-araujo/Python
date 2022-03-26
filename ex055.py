from time import sleep
a=int(input('Digite o primeiro valor:'))
b=int(input('Digite o segundo valor:'))
opção=0
while opção != 5:
    print('''   [1] somar
    [2] multiplicar
    [3] maior
    [4] menor
    [5] sair do programa''')
    opção=int(input('Qual a opção você quer?'))
    if opção ==1:
        s=a+b
        print('A soma é {}'.format(s))
    elif opção==2:
        m=a*b
        print('A multiplicação é {}'.format(m))
    elif opção==3:
        if a>b:
            maior=a
        else:
            maior=b
        print('O maior valor é {}'.format(maior))
    elif opção==4:
        print('Informe os números novamente')
        a = int(input('Digite o primeiro valor:'))
        b = int(input('Digite o segundo valor:'))
    elif opção==5:
        print('Finalizando')
    else:
        print('opção inválida. Tente novamente')
        print('=-='*10)
        sleep(2)
print('Fim!Volte sempre.')
