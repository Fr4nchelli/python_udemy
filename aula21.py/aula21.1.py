# For por baixo dos panos

"""
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter - me entregue seu iterador
"""

# texto = iter('Vinicius') # ___iter___
# print(texto)
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# for letra in texto

texto = 'Luiz' # iterável
iterador = iter(texto) #iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
print()

for letra in texto:
    print(letra)