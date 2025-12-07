#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
n1 = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o comprimento do cateto adjacente: '))
hipo = math.hypot(n1, n2)
print(f'A hipotenusa do seu triângulo retângulo é de {hipo}')