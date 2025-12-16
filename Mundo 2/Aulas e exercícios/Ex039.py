#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = date.today().year

pergunta = int(input('Informe o seu ano de nascimento: '))

idade = ano - pergunta

if idade < 18:
    print(f'Você deverá se alistar daqui a {18-idade}.')
elif idade == 18:
    print('Você deverá se alistar neste ano.')
elif idade > 18:
    print(f'Você deveria ter se alistado em {idade-18} anos atrás, ou seja em {ano - 18}.')