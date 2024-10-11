# Iteração de strings com while

# 0 1 2 3 4 5 6 7 8 9 10

nome = 'vinicius'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'

print(novo_nome)