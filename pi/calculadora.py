# membros do grupo
# joão Oliveira(scrum master)
# daniel Oliveira
# gustavo henryque gomes
# gustavo santos
# joap pedro narcizo

# Grupo QI+

decimal = int(input('digite um numero decimal:'))
base = int(input('qual a base? [2] [8] [16]: '))

digitos = '0123456789ABCDEF'

convertido = ''

while decimal > 0:
    convertido = digitos[decimal%base] + convertido
    decimal = decimal//base

    print(convertido)

