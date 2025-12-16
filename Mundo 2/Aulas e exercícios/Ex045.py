#Crie um programa que faça o computador jogar jookenpô com você.
import random
from time import sleep
print('=-=' * 20)
print('Vamos jogar Jokenpô!')
print('=-=' * 20)

itens = ('Pedra','Papel','Tesoura')
jo = random.randint(0, 2) #Pc pensando em qual irá escolher
pc = itens[jo] #Mudando a escolha do pc para as possíveis opções.

user = int(input('Escolha sua jogada:\n[0] Pedra\n[1] Papel\n[2] Tesoura\nQual é a sua escolha? '))
if user > 2:
    print('tente novamente.')

usuario = lista[user] #mudando o número escolhido pela jogada.

print(f'Você escolheu {usuario} e eu escolhi {pc}')

if user == 0 and jo == 2:
    print(f'{usuario} ganha de {pc}. VOCÊ VENCEU!')
elif user == 1 and jo == 0:
    print(f'{usuario} ganha de {pc}. VOCÊ VENCEU!')
elif user == 2 and jo == 1:
    print(f'{usuario} ganha de {pc}. VOCÊ VENCEU!')
elif user == 0 and jo == 1:
    print(f'{pc} ganha de {usuario}, EU GANHEI!')
elif user == 1 and jo == 2:
    print(f'{pc} ganha de {usuario}, EU GANHEI!')
elif user == 2 and jo == 0:
    print(f'{pc} ganha de {usuario}, EU GANHEI!')
else:
    print('EMPATE')