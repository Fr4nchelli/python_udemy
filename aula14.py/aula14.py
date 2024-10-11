# Formatação básica de strings
"""
s- string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
> - direita
^ - centro
Sinal - + ou -
Ex. : 0>-100,.1f
Conversion flags - !r !s !a

"""
variavel = 'ABC'
print(f'{variavel}')

# pad
# :(sinal desejado)(posição de alinhamento)(quantos caracteres)
variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{variavel:#>10}')
print('-' * 20)
print(f'{1000.31531351853:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')