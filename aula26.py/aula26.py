"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '    Olha só que, coisa interessante'
lista_palavras = frase.split() # Divide a string e cria uma lista com as palavras separadas
print(lista_palavras)
lista_frases = frase.split(',') # Divide a string com a quebra no ','
print(lista_frases)
print(frase.strip()) # Strip retira os espaços do final e começo

frase_1 = ' -'.join(lista_frases) # junta strings listas e tuplas com um separador
print(frase_1)