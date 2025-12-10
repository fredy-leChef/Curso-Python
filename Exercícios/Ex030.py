#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
calc = num % 2
print(f'Você digitou o número {num}')
if calc == 0:
    print(f'O número escolhido é par!')
else:
    print(f'O número escolhido é ímpar.')