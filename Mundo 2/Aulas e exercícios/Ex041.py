#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
#até 9 anos: Mirim
#ATé 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: Sênior
#Cima: Master

from datetime import date

atual = date.today().year

ano = int(input('Informe o ano de nascimento: '))

idade = atual - ano

if idade <= 9:
    print('Você está na categoria MIRIM')
elif idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade <= 20:
    print('Você está na categoria INFANTIL')
else:
    print('Você está na categoria MASTER')