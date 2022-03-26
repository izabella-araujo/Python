a=float(input('Qual sua altura?'))
p=float(input('Qual seu peso?'))
s=p/a**2
print('De acordo com IMC você está:')
if s<18.5:
    print('Abaixo do peso')
elif 18.5<s>=25:
    print('Com peso ideal')
elif 25<s>=30:
    print('Com sobrepeso')
elif 30<s>=40:
    print('Com obsidade')
else:
    print('Com obsidade móbida')
