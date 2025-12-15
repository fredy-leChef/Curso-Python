#Utilizar códigos ANSI para configurar cores em seus programas em python.

#ANSI = escape sequence --> \033[style, text, background m]

#ex: \033[0;33;44m] --> style 0 (nada), text amarelo (33), background azul (44).

#códigos de estilo:
# 0 - none
# 1 - bold
# 4 - underline
# 7 - negative

#códigos de texto:
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - roxo
# 36 - ciano
# 37 - cinza

#códigos de background:
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - roxo
# 46 - ciano
# 47 - cinza

#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[0;30;47m
#\033[m
#\033[7;30;40m

print('\033[31;43mOlá, mundo!\033[m')

#pode-se usar listas para guardar cores
cores = {'Limpa':'\033[m',
        'Vermelho':'\033[31m',
        'Verde':'\033[32m',
        'Amarelo':'\033[33m',
        'Azul':'\033[34m',
        'Roxo':'\033[35m'}

# e usar elas assim:
nome = 'Frederico'
print(f'Olá! Muito prazer em te conhecer {cores["Amarelo"]}{nome}{cores["Limpa"]}!')