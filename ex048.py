#Faça um programa que calcule a soma de todos os numeros impares que são multiplos de 3
# e que se encontram no intervalo entre 1 e 500
s=0
for c in range (0,500):

    if c % 2 != 0 and c % 3 == 0:
        s= s+c

print(s)
