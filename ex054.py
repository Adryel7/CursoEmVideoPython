#Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre quantas ainda
#não atingiram a maior idade e quantas atingiram

from datetime import date
x=0
y=0
for c in range (0,7):
    a=int(input('Insira o ano de nascimento: '))
    i=date.today().year-a
    if i >= 21:
        x=x+1

    else:
        y=y+1

print('{} pessoas ja atinjiram a maior idade e {} pessoas não atingiram a maior idade.'.format(x,y))

