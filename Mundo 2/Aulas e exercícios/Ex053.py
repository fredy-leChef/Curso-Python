#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

a = str(input('Digite uma frase: ')).upper().strip()
palavras = a.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase {a} é um palíndromo!')
else:
    print(f'A frase {a} não é palíndromo!')