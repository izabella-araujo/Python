s=float(input('Qual o seu salário:'))
if s>1250:
    result=s*1.1
    print('O valor do seu salário com aumento é:{}'.format(result))
else:
    valor=s*1.15
    print('O valor do seu salário atual é:{}'.format(valor))
print('--FIM--')

