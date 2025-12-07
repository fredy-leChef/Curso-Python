#Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
n = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print(f'Seno: {sen:.2f}\nCosseno: {cos:.2f}\nTangente: {tan:.2f}')