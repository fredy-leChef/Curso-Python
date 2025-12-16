#Elabore um programa que calclule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# até 2x no cartão: preço normal
# 3x ou mais no cartão 20% de juros.

valor = float(input('Digite o valor do produto: R$'))
metodo = int(input('Escolha a forma de pagamento:\n[1] A vista dinheiro/cheque\n[2] A vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nQual a opção desejada? '))

if metodo == 1:
    valor_final = valor - (valor * 0.10)
    print(f'O valor final do produto é de R${valor_final:.2f} com 10% de desconto.')
elif metodo == 2:
    valor_final = valor - (valor * 0.05)
    print(f'O valor final do produto é de R${valor_final:.2f} com 5% de desconto.')
elif metodo == 3:
    print(f'O valor final do produto é de R${valor:.2f}, duas parcelas de R${valor/2:.2f} sem juros.')
else:
    parcelas = int(input('Quantas parcelas? '))
    valor_final = valor + (valor * 0.20)
    print(f'O valor final do produto é de R${valor_final:.2f}, {parcelas} parcelas de R${valor_final/parcelas:.2f} com 20% de juros.')