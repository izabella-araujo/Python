a=int(input('Digite um número:'))
tot=0
for c in range(1, a+1):
    if a%c==0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print('{}'. format(c), end=' ')
print('0 número {} foi divisível {} vezes'.format(a,tot))
if tot==2:
    print('Por isso o número é primo')
else:
    print('Por isso o número não é primo')

    
