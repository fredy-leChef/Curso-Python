#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro número da PA: '))
r = int(input('Digite a razão da PA: '))
n = 10
an = a1 + (n-1) * r


for i in range (a1, an + r, r):
    print(i)