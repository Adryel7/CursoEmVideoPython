#faça um programa que leia um ano e mostre seu seno, cosse e tangente

import math

a=float(input('Insira o angulo: '))

a=math.radians(a)

s=math.sin(a)
c=math.cos(a)
t=math.tan(a)

a=math.degrees(a)

print(' Os valores de seno, cosseno e tangente do angulo {:.0f}º são respectivamente {:.2f}, {:.2f}, {:.2f}' .format(a, s, c, t))


