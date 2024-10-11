"""
Tipo list - mutável
suporta valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
"""

lista = [10,20,30,40] # lista criada
# numero = lista[2] #variavel criada pegando o valor de indice 2 da lista
# print(numero)
print(lista)

del lista[2] # deleta o valor de indice 2 da lista
print('Del: ',lista)

lista.append(50) # adiciona um valor ao final da lista
print('Append: ',lista)

lista.pop() # remove o ultimo valor da lista, caso informado o indice remove o valor correspondente
print('Pop: ', lista)

lista.insert(-1, 5) # adiciona um valor passando um indice e valor, caso o indice informado for maior que a lista ele envia o valor para o final da lista
print(lista)

#lista.clear() # limpa os valores da lista
#print(lista)