#Condições aninhadas - Uma estrturua aninhnada é chamada assim pois ela se encontra em um formato de ninho, uma dentro da outra.
# if... elif.. else

#O uso do else pode ser opicional, nem sempre eu necessito usar o else usando o elif.
#O uso do elif é indeterminado, entretanto o else é único.


nome = str(input('Qual é seu nome: '))
if nome =='Frederico':
    print('Que nome lindo!')
elif nome in ['Pedro', 'Maria', 'Paulo']: #Nomes colocados em lista para retornar um valor específico para eles.
    print("Seu nome é bem popular no Brasil.")
elif nome in ['Ana', 'Cláudia', 'Jéssica', 'Juliana']:
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')