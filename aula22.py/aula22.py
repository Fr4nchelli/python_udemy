# exercicio da palavra secreta
"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- voce vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuario digitar apenas uma letra.
- quando o usuario digitar uma letra, voce vai conferir se a letra digitada esta na palavra secreta.
- se a letra digitada estiver na palavra secreta; exiba a letra
- se a letra digitada não estiver na palavra secreta; exiba *

faça a contagem de tentativas do seu usuario
"""
import os
print("""                   Bem vindo(a) ao jogo!
      -------------------------------------------------------
                            Regras: 
                 Digite uma letra por vez!
      Uma vez digitada, caso a letra esteja na palavra ela aparecera, caso
      não esteja ficara marcado com *
                            Boa sorte!
      -------------------------------------------------------""")
palavra_secreta = 'python'
letras_acertadas = ''
numero_tentativas = 0

while True:
   letra_digitada = input('Digite uma letra: ')
   numero_tentativas += 1

   if len(letra_digitada) > 1:
      print('Digite apenas uma letra.')
      continue

   if letra_digitada in palavra_secreta:
     letras_acertadas += letra_digitada

   palavra_formada = ''
   for letra_secreta in palavra_secreta:
      if letra_secreta in letras_acertadas:
         palavra_formada += letra_secreta
      else:
         palavra_formada += '*'
   print(palavra_formada)

   if palavra_formada == palavra_secreta:
      os.system('cls')
      print('VOCÊ GANHOU! PARABENS!')
      print('A PALAVRA ERA', palavra_secreta)
      print('TENTATIVAS: ', numero_tentativas)
      numero_tentativas = 0
      letras_acertadas = ''