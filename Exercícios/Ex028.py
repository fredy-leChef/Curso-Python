#Faça um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random as rd

n = int(input('Advinhe um número de 0 a 5 '))
random = rd.randint(0,5)
if n == random:
    print("Acertou miserável!")
else:
    print('EROUUUUU')
