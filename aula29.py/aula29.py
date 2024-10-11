"""
Introdução a funções em python

funções são trechos de códigos usados para replicar coisas 
dentro do nosso codigo, usada para reutilizar codigos que 
usaremos dentro do codigo
por padrão, funções retornam none.
"""

def Print():
    print('função print')

print('print normal')
Print()

def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Maria')