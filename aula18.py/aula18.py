"""
Condições
while(enquanto)
    executa uma ação enquanto uma condição for verdadeira
"""
"""
numero = 0

while numero <= 20:
    numero += 1
    

    if numero == 6:
        print('Não vou mostrar o 6')
        continue

    if numero >= 5 and numero <= 7:
        continue

    print(numero)

    if numero == 10:
        break

print('Acabou')
"""

"""
While dentro de While
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print (f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')
