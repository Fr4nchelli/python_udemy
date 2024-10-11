# While / else
string = 'Qualquer coisa'

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break
    
    print(letra)
    i += 1
else: 
    print('Não tem espaço vazio')
print('Fora do while')

# Caso o while for executado até o final e não for fechado propositalmente ele entra no else
# Caso o laço while seja interrompido ele pula o laço else
