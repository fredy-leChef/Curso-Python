#Exercicio 7: Faça um programa que leia a largura e a altura de uma parece em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada 1,0 litro de tinta
#pinta uma área de 2m².

n1 = float(input('Informe a largura da parede (m): '))
n2 = float(input('Informe a altura da parede (m): '))
a = n1*n2
t = a/2
print(f'Uma parede com {n1}m de largura e {n2}m de altura, possui uma área de {a}m². \nPara pintar essa parede você precisará {t}L de tinta.')

