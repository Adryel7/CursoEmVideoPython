#Crie um programa que leia o nome de uma cidade e dia se ela começa ou não com o nome 'Santo'.

c=input('Digite o nome da Cidade: ')
d=c.lower().split()
print('santo' in d[0])

