# Coletando informações do usuario via terminal

#input('Qual o seu nome? ')  exibe o texto e para a linha até o usuario fazer uma interação

#nome = input('Qual o seu nome? ') # pega uma informação dada pelo usuario e armazena na variavel nome
#print(f'O seu nome é {nome}')

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

#print(f'A soma dos dois números é: {num1 + num2}') # Aqui está somente concatenando, pois o metodo input so retorna str

# Criei uma nova variavel e converti ela para int, pois quando chamada fara a soma e nao a concatenação
int_num1 = int(num1)
int_num2 = int(num2)

print(f'A soma dos dois números é: {int_num1 + int_num2}') 