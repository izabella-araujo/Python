nome=str(input('Qual o seu nome completo?')).strip()
print('Seus nome em maiusculo é {}'.format(nome.upper()))
print('Seus nome em minisculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))



