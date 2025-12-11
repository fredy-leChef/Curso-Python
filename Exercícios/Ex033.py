#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Informe o 1º número: '))
b = int(input('Informe o 2º número: '))
c = int(input('Informe o 3º número: '))
#Teste de quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Teste de quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#Print da resposta
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
