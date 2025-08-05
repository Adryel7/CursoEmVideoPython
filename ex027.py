#Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e ultimo nome separadamente.

nome=input('Escreva seu nome: ')
nd=nome.split()
print('Primeiro nome: {}' .format(nd[0]))

print('Ultimo nome: {}' .format(nd[len(nd)-1]))
