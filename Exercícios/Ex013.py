#Exercício 9: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n1 = float(input('Salário: '))
a = 1+(15/100)
n2 = n1*a
print(f'Seu salário com 15% de reajuste fica em: R${n2:.2f}')
print(f'Um aumento de R${n2-n1:.2f}')

#Exercicio extra: Faça um algoritmo que dê desconto no pagamento no pix, e aumenta o valor caso seja parcelado.
n = float(input('Preço da mercadoria: R$ '))
pix = n - (n * 8 / 100)
parcelado = n + (n * 8 / 100)
print(f'Pagamento a vista ou no pix: R${pix}.\nPagamento parcelado em até 10x de R${parcelado/10:.2f}')

