"""
Tipo list - mutável
suporta valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b # Adiciona os valores de uma lista a outra
print(lista_c)

lista_a.extend(lista_b) 
print(lista_a)