# Faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para
# pinta-la. Parametro 1l=2m²

l=float(input('Insira a largura da parede: '))
a=float(input('Insira a altura da parede: '))
ar=l*a
t=ar/2

print('Para pintar {} metros quadrados de parede é preciso {} litros de tinta' .format(ar,t))
