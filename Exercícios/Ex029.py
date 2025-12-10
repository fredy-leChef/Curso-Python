#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

vel = int(input('Velocidade registrada: '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Você recebeu uma multa de R${multa:.2f} seu arrombado!')
else:
    print('Velocidade dentro do limite.')