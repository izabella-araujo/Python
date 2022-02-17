a=float(input('Qual o seu ano de nascimento?'))
print('SUA CATEGORIA É:')
i=2022-a
if i<=9:
    print('Mirim')
elif 9<i<=14:
    print('Infantil')
elif 14<i<=19:
    print('junior')
elif 19<i==20:
    print('sênior')
else:
    print('Master')

