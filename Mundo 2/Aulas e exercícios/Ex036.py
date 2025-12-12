#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, os salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


valor = float(input('Informe o valor do imóvel? R$'))
salario = float(input('Informe a sua renda mensal? R$'))
anos = int(input("Informe em quantos anos você deseja quitar o empréstimo: "))
n_meses = anos * 12
parcela = valor/ n_meses

if parcela > salario * 0.30:
    print('Empréstimo negado')
else:
    print(f'Seu empréstimo foi aprovado, e suas parcelas serão de R${parcela:.2f} durante {n_meses} meses.')
