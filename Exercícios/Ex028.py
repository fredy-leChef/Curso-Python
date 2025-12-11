#Faça um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

pc = random.randint(0,5) # Faz o pc pensar
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
player = int(input('Em que número estou pensando? ')) #Joogador tentando adivinhar
print('Processando...')
time.sleep(3)
if player == pc:
    print('PARABÉNS! Você acertou miserável!')
else:
    print(f'ERRROUUUU! Eu pensei no número {pc} e não no {player}!')