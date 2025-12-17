#Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0:
        cont = cont + 1 #contador de números da lista
        soma = soma + c #somatório de todos os números da lista
print(f'Há um total de {cont} números ímpares múltiplos de 3 entre 1 e 500, e o somatório desses números é de {soma}')