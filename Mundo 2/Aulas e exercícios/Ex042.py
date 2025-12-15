#Refaça o ex 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isóceles: dois lados iguais
#Escaleno: Todos os lados diferentes.

r1 = int(input('Informe o comprimento da primeira aresta: '))
r2 = int(input('Informe o comprimento da segunda aresta: '))
r3 = int(input('Informe o comprimento da terceira aresta: '))

#Analisando a possibilidade de formar um triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos não podem formar um triâgnulo!')

#Condicionando o tipo do triângulo.
if r1 == r2 and r1 == r3:
    print('Esse triângulo é do tipo Equilátero, ou seja, todos os lados são iguais.')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Esse triângulo é do tipo Isóceles, ou seja, possuem dois lados iguais.')
elif r1 != r2 and r1 != r3 and r2 != r3:
    print('Esse triângulo é do tipo Escaleno, ou seja, todos os lados são diferentes')