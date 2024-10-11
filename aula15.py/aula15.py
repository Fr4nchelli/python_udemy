# Exercicio

"""
Peça ao usuario para digitar seu nome e sua idade
se o nome e a idade forem digitados exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contem (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade
    exiba "Desculpe, você deixou campos vazios"
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')