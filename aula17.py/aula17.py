# Exercícios para fixação

"""
Faça um programa que peça ao usuario para digitar um numero inteiro, 
informe se esse numero é impar ou par. caso o usuario nao digite um numero inteiro, 
informe que não é um numero inteiro
"""
# Ex 1
"""
numero = input('Digite um numero inteiro: ')
if numero.isdigit():
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print(f'O numero {numero} é par!')
    else:
        print(f'o numero {numero} é impar!')
    
else:
    print('Isso não é um numero inteiro!')
"""
"""
Faça um programa que pergunte a hora ao usuário e, 
baseando-se no horário descrito exiba a saudação apropriada.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
# Ex 2
"""
horario = input('Por favor, informe as horas em numeros inteiros: ')
try:
    hora = int(horario)
    if hora >= 0 and hora <= 11:
        print('Bom dia flor do dia!')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde raio de sol!')

    elif hora >= 18 and hora <= 23:
        print('Boa noite luz do luar!')
    else:
        print('Não consegui identificar esse horário :(')
except:
    print('Você não digitou um numero inteiro!')
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 letras escreva "Seu nome é muito grande"
"""
# Ex 3
"""
primeiro_nome = input('Olá! Qual seu primeiro nome? ')
tamanho_nome = len(primeiro_nome)
if tamanho_nome <= 4:
    print('Que nome pequeno!')

elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Nome grandinho hein?!')

else:
    print('Jeová da glória, que exagero!!!')
"""