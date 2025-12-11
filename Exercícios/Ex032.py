#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.#
'''import calendar

ano = int(input('Digite um ano qualquer para descobrir se ele é bissexto: '))

bissexto = calendar.isleap(ano)

if bissexto == True:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')'''

from datetime import date

ano = int(input('Qual ano deseja analisar? Caso queira analisar o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')