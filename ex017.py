#crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
#triangulo retamgulo e calcule sua hipotenusa.

import math
cato=float(input('Insira o comprimento do cateto oposto(em cm): '))
cato2=math.pow(cato, 2)
cata=float(input('Insira o comprimento do cateto adjacente(em cm): '))
cata2=math.pow(cata,2)

hip2= cato2 + cata2

hip=math.sqrt(hip2)

print('A hipotenusa mede {} centimetros.' .format(hip))
