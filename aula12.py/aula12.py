# Operadores logicos
# and (e) or (ou) not (não)

# and- todas as condições precisam ser verdadeiras
# se qualquer condição for falsa, a expressão toda sera avaliada como falsa

"""
entrada = input('[E]ntrar  [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '1'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
"""


# or - qualquer condição verdadeira avalia a expressao inteira como verdadeira

"""
entrada = input('[E]ntrar  [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '1'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
"""

# not - usado para inverter expressões

"""
senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta!')
if not senha:
    print('Digite uma senha!')
"""

# in e not in
# entre e não entre

nome = 'otavio'
print(nome[2]) #a
print('a' in nome)
print('a' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome: 
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')