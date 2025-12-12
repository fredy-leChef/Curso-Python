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
    print(bin(num[2:]))
elif base == 2:
    print(oct(num[2:]))
else:
    print(hex(num[2:]))