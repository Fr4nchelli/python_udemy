# Exercicio de fixação
# utilizando os operadores de if e comparação, faça uma checagem com dois valores dados pelo usuario e imprima qual o maior valor

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor: {primeiro_valor} é maior do que o segundo valor: {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'Primeiro valor: {primeiro_valor} é menor do que o segundo valor: {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'Valores iguais!')


