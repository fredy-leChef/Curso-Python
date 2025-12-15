#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida.
#Média abaixo de 5.0: Reprovado
#Média entre 5 e 6: Recuperação
#Média 7.0 ou superior: Aprovado.

cores = {'Limpa':'\033[m',
        'Vermelho':'\033[31m',
        'Verde':'\033[32m',
        'Amarelo':'\033[33m',
        'Azul':'\033[34m',
        'Roxo':'\033[35m'}

n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))

med = (n1 + n2) / 2

if med >= 7:
    print(f'Parabéns, você está aprovado com uma média de {cores['Verde']}{med:.2f}{cores['Limpa']}')
elif med >= 5 and med <= 6:
    print(f'Sua média é de {cores['Amarelo']}{med}{cores['Limpa']}, você está de recuperação.')
else:
    print(f'Sua média ficou de {cores['Vermelho']}{med}{cores['Limpa']}, você está reprovado.')