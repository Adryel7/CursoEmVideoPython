#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
#atleta e mostre sua categoria de acordo com a idade
#até 9 anos mirim
#de 9 a 14 infantil
#de 14 a 19 junior
#19 a  20 senior
#acima master

from datetime import date

print('='*20,end='')
print('Sistema de categoria de atletas.',end='')
print('='*20)

n=int(input('\nInsira o ano de nascimento do atleta: '))

i=date.today().year-n

if i < 9:
    print('Categoria Mirim.')

elif i >= 9 and i < 14:
    print('Categoria Infantil.')

elif i >=14 and i < 19:
    print('Categoria Junior.')

elif i >= 19 and i < 21:
    print('Categoria Senior.')

elif i>21:
    print('Categoria Master.')
