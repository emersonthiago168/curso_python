# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  E m e r s o n
# -7-6-5-4-3-2-1
nome = 'Emerson'
# print(nome[3])
# print(nome[-4])

# print('r' in nome) # true
# print('Emer' in nome) # true
# print('Z' in nome) # false
# print('zyo' in nome) # false
# print('-' * 10)
# print('son' not in nome) # false
# print('Z' not in nome) # true

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')