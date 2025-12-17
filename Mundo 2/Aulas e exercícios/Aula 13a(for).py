#Aula para inicio dos estudos com laços de repetição. Uma estrutura de controle nova, chamada de laços, iteração ou loop.

#Laço de repetição ou iteração: 
'''Exemplo prático da aula: 
laço c no intervalo(1,10): --> c é a variável de controle. Nesse caso, cirou-se um laço no intervalo entre 1 e 10
    passo                  --> o passo é a ação que será executada no laço.
pega                       --> ação fora do laço, será efetuada após a finalização do laço.
'''

'''for c in range (1,10):
    passo
pega

for c in range (1,10):
    if moeda:
        pega
    passo
    pula
passo
pega'''

#Uma estrutura aninhada pode ter infinitos ifs dentro de um laço. Basta visualizar a identação para saber aonde estão sendo operados.
'''
for c in range (0,6):
    print(c)
print('Fim')

for c in range (6,0,-1):
    print(c)
print('fim')

for c in range (0,6,2):
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range (0, n):
    print(c)
print('Fim')

i = int(input('Digite um número: '))
f = int(input('Digite um número: '))
p = int(input('Digite um número: '))
for c in range (i, f+1, p):
    print(c)
print('Fim')
'''

s = 0
for c in range (0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma dos valores é de: {s}')