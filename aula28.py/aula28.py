# Exercicio Validação de CPF

"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex: 
   10 * 7 = 70
   9 * 4 = 36
   8 * 6 = 48
   7 * 8 = 56
   6 * 2 = 12
   5 * 4 = 20
   4 * 8 = 32
   3 * 9 = 27
   2 * 0 = 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrario disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
"""

cpf = '746.824.890-70'.replace(".", "").replace("-", "").replace(" ", "")
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

"""
Calculo do segundo digito do CPF
colete a soma dos primerios digitos do cpf
MAIS O PRIMERIO DIGITO
multiplicando cada um dos valores por uma 
contagem regressiva começando de 11
"""

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = ((resultado_digito_2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é valido')
else:
    print('CPF  inválido')

