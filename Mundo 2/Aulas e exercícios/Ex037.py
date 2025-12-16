#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
from time import sleep

num = int(input('Digite o número que deseja converter: '))
sleep(1)
print('[1] Para sistema binário')
print('[2] Para sistema octal')
print('[3] Para sistema hexadecimal')
sleep(1)
base = int(input('Qual base você deseja converter? '))
if base == 1:
    print(f'O número {num} em sistema binário é: {num:b}')
elif base == 2:
    print(f'O número {num} em sistema cotal é: {num:o}')
elif base == 3:
    print(f'O numero {num} em sistema hexadecimal é: {num:h}')
else:
    print('Opção inválida. Tente novamente')