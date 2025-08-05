#Faça um programa que que leia o sexo de uma pessoa que só aceite 'm' ou 'f'. Caso esteja errado
#peça a digitação novamente até ter um valor correto

s=0
while s != 'M' and s != 'F':
    s=input('Insira o sexo(M ou F): ').upper()
