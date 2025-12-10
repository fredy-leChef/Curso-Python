#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import calendar

ano = int(input('Digite um ano qualquer para descobrir se ele é bissexto: '))

bissexto = calendar.isleap(ano)

if bissexto == True:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')