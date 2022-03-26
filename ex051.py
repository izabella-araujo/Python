maior=0
menor=0
for c in range(1,6):
    a=float(input('O peso da da pessoa {} é:?'.format(c)))
    if c==1:
        maior=a
        menor=a
    else:
        if a>maior:
            maior=a
        if a<menor:
            menor=a
print('A pessoa mais pesada tem {} quilos'.format(maior))
print('A pessoa mais leve tem {} quilos'.format(menor))


