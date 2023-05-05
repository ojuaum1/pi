# membros do grupo
# joão Oliveira(scrum master)
# daniel Oliveira
# gustavo henryque gomes
# gustavo santos
# joap pedro narcizo

# Grupo QI+

digitos = '0123456789ABCDEF'

while True:
    decimal = int(input('Digite um número decimal: '))
    base = int(input('Qual a base? [2] [8] [16]: '))

    if base not in [2, 8, 16]:
        print('Base inválida.')
    else:
        convertido = ''
        while decimal > 0:
            convertido = digitos[decimal % base] + convertido
            decimal = decimal // base
        print(convertido)
        break


