a=str(input('informe seu sexo [F/M]:')).strip().upper()[0]
while a not in 'FfMm':
    a=str(input('Dados invalidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(a))
