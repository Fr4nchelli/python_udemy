# Exercício de fixação

"""
Faça uma lista de compras com listas
o usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista
não permita o programa quebre com erros de indices inexistentes na lista.
"""
print('Bem vindo(a) a sua lista de compras!\n')
lista_de_compras = []
while True:
    menu = input("""\nSelecione uma opção:
          1 - Adicionar item
          2 - Remover item
          3 - Listar produtos
          4 - Limpar lista
          5 - Sair\n""")
    
    if menu == '1':
        add_item = input('Digite o item que deseja adicionar a lista: ')
        lista_de_compras.append(add_item)

    elif menu == '2':
        if len(lista_de_compras) == 0:
            print('lista vazia!')
        else:
            for indice, item in enumerate(lista_de_compras):
                print(indice, item)
            try:
                del_item = int(input('Digite o indice do item que deseja remover da lista: '))
                del(lista_de_compras[del_item])
            except:
                print('Indice não encontrado!')

    elif menu == '3':
        if len(lista_de_compras) == 0:
            print('lista vazia!')
        else:
            print('Sua lista até o momento: ')
            for indice, item in enumerate(lista_de_compras):
                print(indice, item)

    elif menu == '4':
        if len(lista_de_compras) == 0:
            print('Sua lista já está vazia!')
        else:
            print('Tem certeza que deseja limpar TODA a sua lista? ')
            confirmacao_de_limpeza = input("""
                1 - Sim
                2 - Não\n""")
          
            if confirmacao_de_limpeza == '1':
                print('Limpando lista.....')
                lista_de_compras.clear()
            else:
                print('Operação cancelada!')
    elif menu == '5':
        print('Deseja mesmo sair? ')
        saida = input("""
                1 - Sim
                2 - Não\n""")
        if saida == '1':
            print('Saindo do programa......')
            break
        elif saida == '2':
            print('Que bom ter você por perto!')
        else:
            print('Digite uma opção válida!')
       