#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
from time import sleep

num = int(input('Digite o número que deseja converter: '))
sleep(1)
print('Para sistema binário digite: 1.')
print('Para sistema octal digite: 2.')
print('Para sistema hexadecimal digite: 3.')
sleep(1)
base = int(input('Qual base você deseja converter? '))
if base == 1:
    print(f'O número {num} em sistema binário é: {num:b}')
elif base == 2:
    print(f'O número {num} em sistema cotal é: {num:o}')
else:
    print(f'O numero {num} em sistema hexadecimal é: {num:h}')