# Fatiamento de strings

# 012345678
# ola mundo
#-987654321

# Fatiamento [i:f:p] [::]
#obs: a função len retorna a qtd de caracteres da str

variavel = 'ola mundo'
print(variavel[5]) #retorna um indice especifico da str
print(variavel[4:]) #define um começo para leitura da str, porém não um final
print(variavel[:3]) #define aonde para a leitura da str
print(len(variavel)) #checa o tamanho da str, contagem != de indice por isso retornou 9!
print(variavel[0:9:1]) #define um começo, final, e o passo da contagem, aqui retorna de 1 em 1
print(variavel[0:9:2]) #define um começo, final, e o passo da contagem, aqui retorna de 2 em 2
print(variavel[-1:-10:-1]) #inverte a contagem
