# tuplas + desempacotamento
#é possivel atribuir os valores de uma lista em uma variavel para ter facil acesso a ele
# nome1, nome2, nome3 = ['maria', 'jose', 'joao']
# print(nome2)

#caso nao quisermos acessar todos os nomes, basta utilizar o sinal * que o interpretador ira separar os outros valores do escolhido
nome1, *_ = ['maria', 'jose', 'joao']
print(nome1, _)


# Tupla é um tipo de lista imutavel

nomes = 'maria', 'josé', 'joão' #pode ser criada sem auxilio dos colchetes ou com ()