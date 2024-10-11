# interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Luiz'
preco = 100.500
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

# a interpolação é outra forma de formatar as strings, colocando o sinal de % no final da string e passando os parametros no final
# variavel = 'teste para variavel, string %s, int %d, float %f, hex %x' % ('string', 10, 10.00, %x)