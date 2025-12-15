#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

h = float(input('Informe sua altura (m): '))
g = float(input('Informe seu peso (kg): '))

h2 = h * h
imc = g / h2

if imc <= 18.5:
    print(f'Seu IMC é de {imc:.2f}, ou seja, você está abaixo do seu peso ideal.')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f}, ou seja, você está no seu peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f}, ou seja, você está com sobrepeso.')
elif imc <= 40:
    print(f'Sei IMC é de {imc:.2f}, ou seja, você está obeso.')
else:
    print('SEU GORDO RIDÍCULO')
