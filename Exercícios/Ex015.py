#Exercício 11: Escreva um programa que pergunte a quantidade de Km percorridos por um carro e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantidade de dias: '))
k = float(input('Quantidade de kilometros rodados: '))
diaria = d * 60
km = k * 0.15
print(f'Valor das diárias: R${diaria}\nValor da kilometragem rodada: R${km}\nTotal a ser pago: {diaria + km:.2f}')