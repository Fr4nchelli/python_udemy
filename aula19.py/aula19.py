# Exercicio com While

print('Bem vindo(a) a calculadora!')

while True:
    
    try:
        
        primeiro_numero = input('Digite o primeiro numero: ')
        segundo_numero = input('Digite o segundo numero: ')

        primeiro_num = float(primeiro_numero) # convertendo o primeiro numero para int
        segundo_num = float(segundo_numero) # convertendo o segundo numero para in
        
        # Operações matematicas
        soma = primeiro_num + segundo_num
        subtracao = primeiro_num - segundo_num
        divisao = primeiro_num / segundo_num
        multiplicacao = primeiro_num * segundo_num
        
        print('O que iremos calcular?')
        
        # Criação do menu
        menu = input(f"""Selecione a operação: 
                    1 - Soma 
                    2 - Subtração
                    3 - Divisão
                    4 - Multiplicação 
                    5 - Sair \n""")
        
        # Resultados
        if menu == '1':
            print(f'O resultado de {primeiro_numero} + {segundo_numero} é {soma}')
        elif menu == '2':
            print(f'O resultado de {primeiro_numero} - {segundo_numero} é {subtracao}')
        elif menu == '3':
            print(f'O resultado de {primeiro_numero} / {segundo_numero} é {divisao}')
        elif menu == '4':
            print(f'O resultado de {primeiro_numero} * {segundo_numero} é {multiplicacao}')
        elif menu == '5':
            print('Saindo do programa....')
            break
        else:
            print('Digite uma opção valida!')
    except:
        print('Erro')
