#Crie um programa que leia o nome e o preço de varios produtos, o programa deverá
#perguntar se o usuario quer continuar. Ao final do programa, mostre:
'''Qual o total gasto na compra
Quantos produtos custam mais que 1000 reais
Qual o nome do produto mais barato'''
t=0
m=0
c=0

print('-'*20,end='')
print('Registro de compra.',end='')
print('-'*20)

while True:
    n=input('Insira o nome do produto: ')
    p=float(input('Insira o valor do produto: R$'))

    t+=p

    if c == 0:
        nb=n
        mb=p
        c+=1

    if p > 1000:
        m+=1

    if mb > p:
        nb=n
        mb=p

    contr=input('Deseja continuar (S/N)? ').upper()

    if contr == 'N':
        break
    elif contr != 'S':
        contr=input('Deseja continuar (S/N)? ').upper()

print(f'\nO total gasto foi R${t:.2f}.')
print(f'{m} produtos custam mais de R$1000.00.')
print(f'O item {nb} foi o mais barato da lista.')
