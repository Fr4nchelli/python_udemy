# o que é o print?

print('Olá') # print é uma função usada para "imprimir" algo na tela

# dentro da função print podemos definir algumas configurações como alterar o separador ou até mesmo definir a quebra de linha

print("teste", "teste", sep="-") # como pode se ver aqui, o separador padrão foi alterado de um simples espaço para uma barra

print("aloha", "mahalo", sep=" ") #caso não definido ele utiliza o espaço em branco como separador

print("aloha", "mahalo", sep=" ", end="*") # o "end" é utilizada para definir o que aparecera no final do codigo impresso
print("aloha", "mahalo", sep=" ", end="*") # caso vazio uma quebra de linha será aplicada

# o código da quebra de linha é "\n"