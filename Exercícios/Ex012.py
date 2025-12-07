#Exercício 8: Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto.
n1 = float(input('Valor do produto? R$ '))
n2 = float(input('Porcentagem de desconto: '))
n3 = 1-(n2/100)
n4 = n1*n3
print(f'Valor com desconto: R${n4}')
print(f'Você economizou: R${n1-n4:.2f}')

