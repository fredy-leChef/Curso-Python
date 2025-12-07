
#Excercício 4: Escreva um programa que leia um valor em metros e exiba convertido em centrímetros e milímetros.

n = float(input('Digite um valor: '))
print(f'A medida de {n}m corresponde a \n{n*0.001}km \n{n*0.01}hm \n{n*0.1:.1f}dam \n{n*10}dm \n{n*100}cm \n{n*1000}mm')

