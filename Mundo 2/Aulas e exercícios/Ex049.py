#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite o valor para saber a tabuada: '))

for c in range (0,11):
    tabuada = num * c
    print(f'{num} * {c} = {tabuada}')