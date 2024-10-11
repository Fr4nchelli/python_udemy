
# F-Strings 
# uma forma de mantermos o código menos poluido e mais dinamico é com as f-strings

nome = 'Vinicius Francelli'
altura = 1.80
peso = 56
imc = peso / (altura * 2)

print(nome, "tem", altura, "de altura,")
print('pesa', peso, 'quilos', 'e seu IMC é ')
print(imc)

resultado_imc = f'{nome} tem {altura:.2f} de altura,\n pesa {peso} quilos, e seu IMC é \n {imc} '
print(resultado_imc)

# Função Format
# Outra forma para formatar 

a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={}'.format(a,b,c)
print(formato)
