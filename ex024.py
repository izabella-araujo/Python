nome=str(input('Digite o seu nome completo:')).strip()
print('Muito prazer em te conhecer')
divisao=nome.split()
print('Seu primeiro nome é {}'.format(divisao[0]))
print('Seu ultimo nome é {}'.format(divisao[len(divisao)-1]))

