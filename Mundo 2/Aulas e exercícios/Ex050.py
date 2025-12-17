# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsider-o.


soma = 0
for i in range (1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 1:
        num = 0
    soma = soma + num
print(soma)