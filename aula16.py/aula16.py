"""
Introdução ao try/except

try - tentar executar o código
except - ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que você digitar: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Isso não é um numero!')

try:
    if numero_str.isdigit():
        numero_float = float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um numero!')